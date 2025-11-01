import json
import re

class EquipmentManager:
    def __init__(self, data_manager):
        self.data = data_manager
        self.file = "equipment.json"

        # Dữ liệu mẫu nếu chưa có file
        self.default_data = {
            "I.Máy Cardio": [
                {"name": "Máy chạy bộ điện", "quantity": 3},
                {"name": "Xe đạp tập", "quantity": 2}
            ],
            "II.Máy tập sức mạnh": [
                {"name": "Máy ép ngực", "quantity": 2},
                {"name": "Máy đạp chân", "quantity": 2},
                {"name": "Máy tập bụng", "quantity": 2}
            ],
            "III.Tạ tự do & Khu vực chức năng": [
                {"name": "Bộ tạ tay", "quantity": 1},
                {"name": "Ghế tập tạ đa năng", "quantity": 3},
                {"name": "Khung gánh tạ", "quantity": 2}
            ]
        }

        # Nếu chưa có file, tạo mặc định
        try:
            self.equipments = self.data.load_json(self.file)
            if not self.equipments:
                self.equipments = self.default_data
                self.data.save_json(self.equipments, self.file)
        except:
            self.equipments = self.default_data
            self.data.save_json(self.equipments, self.file)

    # =========================
    # THUỘC TÍNH 1: HIỂN THỊ
    # =========================
    def show_equipment(self):
        print("\n========== CƠ SỞ VẬT CHẤT PHÒNG TẬP ==========")
        for category, items in self.equipments.items():
            print(f"\n{category}:")
            for eq in items:
                print(f"  - {eq['name']}  |  Số lượng: {eq['quantity']}")
        print("===============================================")

    # =========================
    # THUỘC TÍNH 2: CẬP NHẬT
    # =========================
    def update_equipment(self):
        print("\n========== CẬP NHẬT CƠ SỞ VẬT CHẤT ==========")
        print("Nhập theo cú pháp: +<số lượng> <tên thiết bị> -<nhóm I/II/III>")
        print("Ví dụ: +2 Xe đạp tập -I   hoặc   +1 Máy đẩy vai -II")
        print("Nhập '0' để quay lại menu.\n")

        while True:
            user_input = input("Nhập lệnh cập nhật: ").strip()
            if user_input == "0":
                print("⬅️  Quay lại Menu Admin.")
                break

            # Phân tích cú pháp: +2 Xe đạp tập -II
            match = re.match(r"^\+(\d+)\s+(.+?)(?:\s*-\s*(I{1,3}))?$", user_input, re.IGNORECASE)
            if not match:
                print("❌ Cú pháp không hợp lệ! Hãy thử lại.")
                continue

            quantity = int(match.group(1))
            name = match.group(2).strip()
            group = match.group(3)

            if not group:
                # Nếu không ghi nhóm, tự động tìm trong dữ liệu
                group = self._find_group_by_keyword(name)

            if not group:
                print("❌ Không xác định được nhóm thiết bị (I, II, III).")
                continue

            category = self._resolve_category_name(group)
            added = False

            # Tìm xem thiết bị có sẵn chưa
            for eq in self.equipments[category]:
                if self._normalize(name) in self._normalize(eq['name']):
                    eq['quantity'] += quantity
                    added = True
                    print(f"✅ Đã cập nhật: {eq['name']} (+{quantity})")
                    break

            if not added:
                # Nếu là máy mới → thêm vào
                self.equipments[category].append({"name": name.title(), "quantity": quantity})
                print(f"🆕 Đã thêm máy mới: {name.title()} vào nhóm {category}")

            self.data.save_json(self.equipments, self.file)

    # =========================
    # THUỘC TÍNH 3: XÓA
    # =========================
    def remove_equipment(self):
        print("\n========== XÓA CƠ SỞ VẬT CHẤT ==========")
        self.show_equipment()

        while True:
            name = input("\nNhập tên máy cần xóa (hoặc '0' để quay lại): ").strip()
            if name == "0":
                break

            found = False
            for category, items in self.equipments.items():
                for eq in items:
                    if self._normalize(name) in self._normalize(eq["name"]):
                        print(f"\n{eq['name']} - Số lượng hiện tại: {eq['quantity']}")
                        try:
                            remove_num = int(input("Nhập số lượng muốn xóa: "))
                            if remove_num > eq["quantity"]:
                                print("\n⚠️ Số lượng vượt quá hiện có!")
                                print("1. Nhập lại số lượng máy tập")
                                print("2. Quay lại Menu Admin")
                                print("0. Đăng xuất")
                                opt = input("Chọn: ")
                                if opt == "1":
                                    continue
                                elif opt == "2" or opt == "0":
                                    return
                            else:
                                eq["quantity"] -= remove_num
                                if eq["quantity"] == 0:
                                    items.remove(eq)
                                    print("🗑️ Đã xóa hoàn toàn thiết bị khỏi danh sách.")
                                else:
                                    print(f"✅ Đã giảm {remove_num}. Còn lại {eq['quantity']}.")
                                self.data.save_json(self.equipments, self.file)
                        except ValueError:
                            print("❌ Vui lòng nhập số hợp lệ.")
                        found = True
                        break
                if found:
                    break

            if not found:
                print("❌ Không tìm thấy thiết bị trong danh sách!")

    # =========================
    # HÀM HỖ TRỢ
    # =========================
    def _normalize(self, text):
        """Chuẩn hóa chuỗi để so sánh từ khóa"""
        return re.sub(r"[^a-zA-Z0-9à-ỹ]", "", text.lower())

    def _find_group_by_keyword(self, name):
        """Tự động nhận nhóm I/II/III theo từ khóa"""
        for group, items in self.equipments.items():
            for eq in items:
                if self._normalize(name) in self._normalize(eq["name"]):
                    return group.split(".")[0].replace("I", "I")
        return None

    def _resolve_category_name(self, group_code):
        """Trả lại tên nhóm đầy đủ"""
        mapping = {
            "I": "I.Máy Cardio",
            "II": "II.Máy tập sức mạnh",
            "III": "III.Tạ tự do & Khu vực chức năng"
        }
        return mapping.get(group_code.upper(), "I.Máy Cardio")
