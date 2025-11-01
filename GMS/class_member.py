import json

class MemberManager:
    def __init__(self, data_manager):
        self.data = data_manager
        self.file = "members.json"

        # Dữ liệu mẫu nếu chưa có
        self.default_data = [
            {
                "id": "M001",
                "name": "Nguyễn Văn A",
                "age": 25,
                "gender": "Nam",
                "package": "Gói tháng",
                "trainer": "Trần HLV 1",
                "attendance": 5,
                "paid": True
            },
            {
                "id": "M002",
                "name": "Lê Thị B",
                "age": 28,
                "gender": "Nữ",
                "package": "Gói 7 ngày",
                "trainer": "Nguyễn HLV 2",
                "attendance": 2,
                "paid": False
            }
        ]

        try:
            self.members = self.data.load_json(self.file)
            if not self.members:
                self.members = self.default_data
                self.data.save_json(self.members, self.file)
        except:
            self.members = self.default_data
            self.data.save_json(self.members, self.file)

    # =========================
    # 1. Xem danh sách hội viên
    # =========================
    def show_members(self):
        print("\n========== DANH SÁCH HỘI VIÊN ==========")
        for m in self.members:
            status = " Đã thanh toán" if m["paid"] else " Chưa thanh toán"
            print(f"\nID: {m['id']}")
            print(f"Họ tên: {m['name']}")
            print(f"Tuổi: {m['age']} | Giới tính: {m['gender']}")
            print(f"Gói đăng ký: {m['package']} | HLV: {m['trainer']}")
            print(f"Điểm danh: {m['attendance']} buổi | {status}")
        print("========================================")

    # =========================
    # 2️. Thêm hội viên mới
    # =========================
    def add_member(self):
        print("\n Thêm hội viên mới:")
        new_id = f"M{len(self.members) + 1:03}"
        name = input("Họ tên: ")
        age = int(input("Tuổi: "))
        gender = input("Giới tính (Nam/Nữ): ")
        package = input("Gói đăng ký: ")
        trainer = input("Huấn luyện viên phụ trách: ")
        paid = input("Đã thanh toán? (y/n): ").lower() == "y"

        new_member = {
            "id": new_id,
            "name": name.title(),
            "age": age,
            "gender": gender.capitalize(),
            "package": package,
            "trainer": trainer,
            "attendance": 0,
            "paid": paid
        }

        self.members.append(new_member)
        self.data.save_json(self.members, self.file)
        print(f" Đã thêm hội viên {name.title()} (ID: {new_id})")

    # =========================
    # 3️. Cập nhật thông tin
    # =========================
    def update_member(self):
        self.show_members()
        mem_id = input("\nNhập ID hội viên cần cập nhật: ").strip().upper()
        member = next((m for m in self.members if m["id"] == mem_id), None)

        if not member:
            print(" Không tìm thấy hội viên.")
            return

        print("\nCập nhật thông tin (nhấn Enter để giữ nguyên):")
        name = input(f"Tên ({member['name']}): ") or member["name"]
        package = input(f"Gói tập ({member['package']}): ") or member["package"]
        trainer = input(f"HLV ({member['trainer']}): ") or member["trainer"]
        paid = input("Đã thanh toán? (y/n): ").lower()

        member["name"] = name.title()
        member["package"] = package
        member["trainer"] = trainer
        if paid in ["y", "n"]:
            member["paid"] = (paid == "y")

        self.data.save_json(self.members, self.file)
        print(f" Đã cập nhật thông tin hội viên {member['name']}.")

    # =========================
    # 4️. Xóa hội viên
    # =========================
    def remove_member(self):
        self.show_members()
        mem_id = input("\nNhập ID hội viên cần xóa: ").strip().upper()
        for m in self.members:
            if m["id"] == mem_id:
                self.members.remove(m)
                self.data.save_json(self.members, self.file)
                print(f" Đã xóa hội viên {m['name']}.")
                return
        print(" Không tìm thấy hội viên cần xóa.")
