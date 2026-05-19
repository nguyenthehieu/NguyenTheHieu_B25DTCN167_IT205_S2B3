ten_benh_nhan = input("Nhập họ và tên bệnh nhân: ")
tuoi = int(input("Nhập tuổi bệnh nhân: "))

if ten_benh_nhan.strip() == "" or tuoi < 0 or tuoi > 150:
    print("Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")

else:

    if tuoi < 6:
        ket_qua = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."

    elif tuoi >= 80:
        ket_qua = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."

    else:
        ket_qua = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."

    print("\nPHIẾU KHÁM BỆNH")
    print("Tên bệnh nhân:", ten_benh_nhan)
    print("Tuổi:", tuoi)
    print("Kết quả phân luồng:")
    print(ket_qua)