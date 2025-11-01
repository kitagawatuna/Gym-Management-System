from equipment_manager import EquipmentManager
from TrainerManager import TrainerManager

class Admin:
    def __init__(self, admin_id, name, data_manager):
        self.admin_id = admin_id
        self.name = name
        self.data = data_manager
        self.equipment_manager = EquipmentManager(data_manager)
        self.trainer_manager = TrainerManager(data_manager)

    def show_menu(self):
        while True:
            print("\n========== MENU ADMIN ==========")
            print("1. Quản lý cơ sở vật chất phòng tập")
            print("2. Quản lý huấn luyện viên")
            print("3. Quản lý gói đăng ký")
            print("4. Tạo báo cáo doanh thu & điểm danh")
            print("5. Quản lý hồ sơ hội viên")
            print("0. Đăng xuất")
            print("================================")

            choice = input("Chọn chức năng: ")

            if choice == "1":
                self.equipment_manager_menu()   #  Gọi menu quản lý cơ sở vật chất
            elif choice == "2":
                self.trainer_manager_menu()
            elif choice == "3":
                print("\n[📦] Đang mở chức năng quản lý gói đăng ký...")
            elif choice == "4":
                print("\n[📊] Đang mở chức năng báo cáo doanh thu & điểm danh...")
            elif choice == "5":
                print("\n[👥] Đang mở chức năng quản lý hồ sơ hội viên...")
            elif choice == "0":
                print("\n🚪 Đăng xuất thành công!")
                break
            else:
                print("❌ Lựa chọn không hợp lệ, vui lòng nhập lại.")
    def equipment_manager_menu(self):   # 🔹 Thêm toàn bộ đoạn này ở cuối file
        while True:
            print("\n====== QUẢN LÝ CƠ SỞ VẬT CHẤT ======")
            print("1. Xem cơ sở vật chất")
            print("2. Cập nhật cơ sở vật chất")
            print("3. Xóa cơ sở vật chất")
            print("0. Quay lại Menu Admin")
            print("====================================")
            opt = input("Chọn: ").strip()
            if opt == "1":
                self.equipment_manager.show_equipment()
            elif opt == "2":
                self.equipment_manager.update_equipment()
            elif opt == "3":
                self.equipment_manager.remove_equipment()
            elif opt == "0":
                break
            else:
                print("❌ Lựa chọn không hợp lệ.")
    def trainer_manager_menu(self):
       while True:
        print("\n====== QUẢN LÝ HUẤN LUYỆN VIÊN ======")
        print("1. Xem hồ sơ Huấn luyện viên")
        print("2. Cập nhật hồ sơ Huấn luyện viên")
        print("3. Xóa Huấn luyện viên")
        print("4. Khôi phục Huấn luyện viên (Lịch sử xóa)")
        print("5. Thêm hồ sơ Huấn luyện viên")  # 🟢 Thêm dòng này
        print("0. Quay lại Menu Admin")
        print("======================================")

        opt = input("Chọn: ").strip()

        if opt == "1":
            self.trainer_manager.show_trainers()
        elif opt == "2":
            self.trainer_manager.update_trainer()
        elif opt == "3":
            self.trainer_manager.remove_trainer()
        elif opt == "4":
            self.trainer_manager.restore_trainer()
        elif opt == "5":
            self.trainer_manager.add_trainer()  # 🟢 Gọi hàm bạn đã tạo
        elif opt == "0":
            break
        else:
            print("❌ Lựa chọn không hợp lệ.")

