import json
import re
from datetime import datetime

class TrainerManager:
    def __init__(self, data_manager):
        self.data = data_manager
        self.file = "trainers.json"
        self.deleted_file = "deleted_trainers.json"

        # ===============================
        # 🔹 Dữ liệu mẫu (3 huấn luyện viên)
        # ===============================
        self.default_trainers = [
            {
                "name": "Nguyễn Văn An",
                "birth_year": 2002,
                "gender": "Nam",
                "phone": "0912345678",
                "email": "annguyen123@email.com",
                "address": "TP. Hồ Chí Minh",
                "experience": "1 năm",
                "workplace": "Fitness Plus Center (Hà Nội)",
                "current_member": "Phạm Thanh Tuấn"
            },
            {
                "name": "Phạm Hoàng Long",
                "birth_year": 1998,
                "gender": "Nam",
                "phone": "0987654321",
                "email": "longpham@email.com",
                "address": "Đà Nẵng",
                "experience": "2 năm",
                "workplace": "California Fitness",
                "current_member": "Trương Nhất Linh"
            },
            {
                "name": "Lê Minh Thư",
                "birth_year": 2000,
                "gender": "Nữ",
                "phone": "0905123456",
                "email": "thuleminh@email.com",
                "address": "Hà Nội",
                "experience": "Mới vào",
                "workplace": "GymCenter Elite",
                "current_member": "Phạm Nguyên Khánh"
            }
        ]

        # Nếu chưa có file trainers.json, tự tạo mới
        try:
            self.trainers = self.data.load_json(self.file)
            if not self.trainers:
                self.trainers = self.default_trainers
                self.data.save_json(self.trainers, self.file)
        except:
            self.trainers = self.default_trainers
            self.data.save_json(self.trainers, self.file)

    # ======================================================
    # 🧩 THUỘC TÍNH 1: XEM HỒ SƠ HUẤN LUYỆN VIÊN
    # ======================================================
    def show_trainers(self):
        print("\n========== QUẢN LÝ HUẤN LUYỆN VIÊN ==========")
        print(f"Số lượng huấn luyện viên hiện có: {len(self.trainers)}\n")

        for idx, t in enumerate(self.trainers, start=1):
            print(f"{idx}. Họ và tên: {t['name']}")
            print(f"   Năm sinh: {t['birth_year']}")
            print(f"   Giới tính: {t['gender']}")
            print(f"   Số điện thoại: {t['phone']}")
            print(f"   Email: {t['email']}")
            print(f"   Địa chỉ: {t['address']}\n")

            print("   II. Chuyên môn & Kinh nghiệm:")
            print(f"   - Kinh nghiệm làm việc: {t['experience']}")
            print(f"   - Nơi đã làm việc: {t['workplace']}")
            print(f"   - Đang huấn luyện học viên: {t['current_member']}")
            print("---------------------------------------------------")
        print("===============================================")

    # ======================================================
    # 🧩 THUỘC TÍNH 2: CẬP NHẬT HỒ SƠ HUẤN LUYỆN VIÊN
    # ======================================================
    def update_trainer(self):
        print("\n========== CẬP NHẬT HỒ SƠ HUẤN LUYỆN VIÊN ==========")

        # 🟢 Hiển thị danh sách huấn luyện viên hiện có
        print("\nDanh sách huấn luyện viên hiện có:")
        for idx, t in enumerate(self.trainers, start=1):
            print(f"{idx}. {t['name']}")
        print("--------------------------------------")

        # 🟢 Cho phép admin nhập tên hoặc số thứ tự
        name_or_index = input("Nhập tên hoặc số thứ tự huấn luyện viên cần cập nhật: ").strip()

        trainer = None
        # Nếu admin nhập số thứ tự
        if name_or_index.isdigit():
            index = int(name_or_index) - 1
            if 0 <= index < len(self.trainers):
                trainer = self.trainers[index]
        else:
            # Nếu admin nhập tên
            trainer = next(
                (t for t in self.trainers if self._normalize(name_or_index) in self._normalize(t["name"])),
                None
            )

        if not trainer:
            print("❌ Không tìm thấy huấn luyện viên.")
            return

        # 🟢 Bắt đầu cập nhật thông tin
        print("\nI. Thông tin cá nhân")
        print("II. Chuyên môn & Kinh nghiệm")
        choice = input("Nhập mục bạn muốn cập nhật (I/II hoặc 1/2): ").strip().lower()

        if choice in ["i", "1"]:
            print("\n1. Họ và tên\n2. Năm sinh\n3. Giới tính\n4. Số điện thoại\n5. Email\n6. Địa chỉ")
            field_choice = input("Chọn thuộc tính cần cập nhật: ").strip().lower()

            mapping = {
                "1": "name", "2": "birth_year", "3": "gender",
                "4": "phone", "5": "email", "6": "address",
                "một": "name", "hai": "birth_year", "ba": "gender",
                "bốn": "phone", "năm": "email", "sáu": "address"
            }

            key = mapping.get(field_choice)
            if key:
                new_value = input(f"Nhập giá trị mới cho {key}: ")
                trainer[key] = new_value
                print("✅ Đã cập nhật thông tin thành công!")
            else:
                print("❌ Lựa chọn không hợp lệ.")

        elif choice in ["ii", "2"]:
            print("\n1. Kinh nghiệm làm việc\n2. Nơi đã làm việc")
            sub_choice = input("Bạn muốn cập nhật: ").strip().lower()
            if sub_choice in ["1", "một"]:
                new_value = input("Cập nhật kinh nghiệm làm việc: ")
                trainer["experience"] = new_value
            elif sub_choice in ["2", "hai"]:
                new_value = input("Cập nhật nơi đã làm việc: ")
                trainer["workplace"] = new_value
            else:
                print("❌ Lựa chọn không hợp lệ.")
            print("✅ Đã cập nhật thành công!")

        else:
            print("❌ Lựa chọn không hợp lệ.")

        # 🟢 Lưu thay đổi
        self.data.save_json(self.trainers, self.file)

   

    # ======================================================
    # 🧩 THUỘC TÍNH 3: XÓA HUẤN LUYỆN VIÊN + LỊCH SỬ & KHÔI PHỤC
    # ======================================================
    def remove_trainer(self):
        """
        🔹 Chức năng: 'Xóa' huấn luyện viên (đánh dấu là INACTIVE thay vì xóa thật).
        🔹 Mục tiêu: Giữ toàn bộ thông tin để có thể khôi phục khi cần.
        """

        print("\n========== XÓA HUẤN LUYỆN VIÊN ==========")
        # Lọc ra các huấn luyện viên đang hoạt động
        active_trainers = [t for t in self.trainers if t.get("status", "active") == "active"]

        if not active_trainers:
            print("⚠️  Không có huấn luyện viên nào đang hoạt động.")
            return

        # Hiển thị danh sách huấn luyện viên hiện có
        for idx, t in enumerate(active_trainers, start=1):
            print(f"{idx}. {t['name']}  (Mã: {t.get('trainer_id','N/A')})")
        print("--------------------------------------")

        choice = input("Chọn huấn luyện viên bạn muốn xóa (nhập số, 0 để hủy): ").strip()
        if choice == "0":
            print("➡️ Hủy thao tác xóa.")
            return

        try:
            index = int(choice) - 1
            if 0 <= index < len(active_trainers):
                trainer = active_trainers[index]

                # Đánh dấu là "inactive" thay vì xóa
                trainer["status"] = "inactive"
                trainer["deleted_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Ghi thay đổi vào file JSON
                self.data.save_json(self.trainers, self.file)

                print(f"🗑️ Huấn luyện viên {trainer['name']} đã được chuyển sang trạng thái INACTIVE.")
                print("🔔 Bạn có thể khôi phục lại trong mục 'Lịch sử xóa & Khôi phục'.")
            else:
                print("❌ Số không hợp lệ.")
        except ValueError:
            print("❌ Vui lòng nhập số hợp lệ.")


    # ======================================================
    # 🧩 THUỘC TÍNH 4: LỊCH SỬ XÓA & KHÔI PHỤC HUẤN LUYỆN VIÊN
    # ======================================================
    def restore_trainer(self):
        """
        🔹 Chức năng: Hiển thị danh sách huấn luyện viên bị xóa (inactive)
        và cho phép admin khôi phục.
        🔹 Khi khôi phục, trainer trở lại 'active'
        và cập nhật toàn bộ members có trainer_id trùng để đồng bộ.
        """

        print("\n========== LỊCH SỬ XÓA & KHÔI PHỤC HUẤN LUYỆN VIÊN ==========")
        inactive_trainers = [t for t in self.trainers if t.get("status") == "inactive"]

        if not inactive_trainers:
            print("✅ Không có huấn luyện viên nào cần khôi phục.")
            return

        # Hiển thị danh sách các trainer bị xóa
        for idx, t in enumerate(inactive_trainers, start=1):
            deleted_time = t.get("deleted_at", "Không xác định")
            print(f"{idx}. {t['name']}  (Mã: {t.get('trainer_id','N/A')})  |  Xóa lúc: {deleted_time}")
        print("--------------------------------------")

        choice = input("Chọn huấn luyện viên bạn muốn khôi phục (nhập số, 0 để hủy): ").strip()
        if choice == "0":
            print("➡️ Hủy khôi phục.")
            return

        try:
            index = int(choice) - 1
            if 0 <= index < len(inactive_trainers):
                trainer = inactive_trainers[index]

                # Cập nhật trạng thái và xóa dấu thời gian xóa
                trainer["status"] = "active"
                trainer.pop("deleted_at", None)
                self.data.save_json(self.trainers, self.file)

                # 🔄 Cập nhật lại file members.json
                try:
                    members = self.data.load_json("members.json")
                    for m in members:
                        if m.get("trainer_id") == trainer.get("trainer_id"):
                            m["trainer_status"] = "active"
                    self.data.save_json(members, "members.json")
                except Exception as e:
                    print(f"⚠️ Không thể cập nhật thành viên liên quan: {e}")

                print(f"✅ Đã khôi phục huấn luyện viên: {trainer['name']}")
            else:
                print("❌ Số không hợp lệ.")
        except ValueError:
            print("❌ Vui lòng nhập số hợp lệ.")

    # ======================================================
    # 🧩 THUỘC TÍNH 5: THÊM HỒ SƠ HUẤN LUYỆN VIÊN
    # ======================================================
    def add_trainer(self):
        """
        🔹 Chức năng: Tạo mới hồ sơ huấn luyện viên.
        🔹 Admin nhập các thông tin cơ bản → hệ thống tự tạo trainer_id.
        🔹 Hồ sơ mới sẽ được lưu vào trainers.json.
        """

        print("\n========== THÊM HỒ SƠ HUẤN LUYỆN VIÊN ==========")

        # Tạo trainer_id tự động (dựa theo số lượng trainer hiện có)
        new_id = f"T{len(self.trainers) + 1:03d}"

        # Nhập thông tin cá nhân
        name = input("Nhập họ và tên: ").strip()
        birth_year = input("Nhập năm sinh: ").strip()
        gender = input("Nhập giới tính (Nam/Nữ): ").strip()
        phone = input("Nhập số điện thoại: ").strip()
        email = input("Nhập email: ").strip()
        address = input("Nhập địa chỉ: ").strip()

        # Nhập thông tin chuyên môn
        experience = input("Nhập kinh nghiệm làm việc: ").strip()
        workplace = input("Nhập nơi đã làm việc: ").strip()
        current_member = input("Huấn luyện viên hiện đang huấn luyện học viên (nếu có): ").strip()

        # Tạo hồ sơ trainer mới
        new_trainer = {
            "trainer_id": new_id,
            "name": name,
            "birth_year": birth_year,
            "gender": gender,
            "phone": phone,
            "email": email,
            "address": address,
            "experience": experience,
            "workplace": workplace,
            "current_member": current_member if current_member else "Chưa có",
            "status": "active"
        }

        # Lưu vào danh sách và ghi ra file
        self.trainers.append(new_trainer)
        self.data.save_json(self.trainers, self.file)

        print(f"\n✅ Đã thêm huấn luyện viên mới: {name}")
        print(f"📋 Mã huấn luyện viên: {new_id}")
        print("=============================================")
