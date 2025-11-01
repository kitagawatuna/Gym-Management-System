from data_manager import DataManager
from admin import Admin

def main():
    data = DataManager()

    print("========================================")
    print("   CHÀO MỪNG ĐẾN HỆ THỐNG GYM MANAGEMENT")
    print("========================================\n")

    print("Chọn vai trò đăng nhập:")
    print("----------------------------------------")
    print(" 001 - Admin")
    print(" 002 - Trainer")
    print(" 003 - Member")
    print("----------------------------------------")

    role = input("👉 Nhập mã vai trò của bạn (001 / 002 / 003): ").strip()

    if role == "001":
        password = input("\n🔑 Nhập mật khẩu admin: ").strip()
        if password == "admin111":
            print("\n✅ Đăng nhập thành công với vai trò: ADMIN")
            admin = Admin("A001", "Lâm Nhựt Huy", data)
            admin.show_menu()
        else:
            print("❌ Sai mật khẩu! Đăng nhập thất bại.")

    elif role == "002":
        password = input("\n🔑 Nhập mật khẩu trainer: ").strip()
        if password == "trainer111":
            print("\n✅ Đăng nhập thành công với vai trò: TRAINER")
            print("👉 (Chức năng Trainer sẽ được xây dựng sau)")
        else:
            print("❌ Sai mật khẩu!")

    elif role == "003":
        password = input("\n🔑 Nhập mật khẩu member: ").strip()
        if password == "member111":
            print("\n✅ Đăng nhập thành công với vai trò: MEMBER")
            print("👉 (Chức năng Member sẽ được xây dựng sau)")
        else:
            print("❌ Sai mật khẩu!")

    else:
        print("\n❌ Mã vai trò không hợp lệ!")

if __name__ == "__main__":
    main()
