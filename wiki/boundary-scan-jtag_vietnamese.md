# Boundary Scan (JTAG)

## 1. Định nghĩa: **Boundary Scan (JTAG)** là gì?
**Boundary Scan (JTAG)**, viết tắt của Joint Test Action Group, là một tiêu chuẩn kỹ thuật được phát triển để kiểm tra và gỡ lỗi các mạch tích hợp (IC) và các hệ thống điện tử phức tạp. Được giới thiệu lần đầu vào năm 1985, JTAG đã trở thành một phần không thể thiếu trong quy trình thiết kế và sản xuất VLSI (Very Large Scale Integration). 

Cốt lõi của **Boundary Scan** là khả năng kiểm tra các tín hiệu tại các điểm giao tiếp giữa các mạch tích hợp mà không cần truy cập vật lý vào các chân của chip. Điều này được thực hiện thông qua việc thêm các bộ chuyển đổi (tap) vào các chân của IC, cho phép các tín hiệu được truyền qua các đường dẫn kiểm tra riêng biệt. Với khả năng này, **Boundary Scan (JTAG)** không chỉ hỗ trợ trong việc kiểm tra các lỗi sản xuất mà còn giúp trong việc gỡ lỗi các thiết kế phức tạp trong quá trình phát triển.

Một trong những lợi ích chính của **Boundary Scan (JTAG)** là khả năng thực hiện kiểm tra trên các bo mạch mà không cần tháo rời chúng. Điều này giúp giảm thời gian và chi phí sản xuất, đồng thời tăng tính chính xác trong quy trình kiểm tra. Hơn nữa, **Boundary Scan** cũng hỗ trợ việc phát hiện các lỗi trong quá trình lắp ráp và hàn, cũng như trong các giai đoạn hoạt động của mạch.

Kỹ thuật này cũng rất quan trọng trong việc phát triển các hệ thống nhúng (embedded systems), nơi mà việc kiểm tra và gỡ lỗi các thiết kế phần cứng phức tạp là rất cần thiết. Nhờ vào khả năng tương tác với các thiết bị khác thông qua các giao thức chuẩn, **Boundary Scan (JTAG)** đã trở thành một công cụ quan trọng trong lĩnh vực thiết kế và sản xuất điện tử hiện đại.

## 2. Thành phần và Nguyên lý hoạt động
**Boundary Scan (JTAG)** bao gồm nhiều thành phần chính, mỗi thành phần đóng một vai trò quan trọng trong việc thực hiện các chức năng kiểm tra và gỡ lỗi. Các thành phần chính bao gồm:

1. **TAP Controller (Test Access Port Controller)**: Đây là bộ điều khiển trung tâm của JTAG, có nhiệm vụ quản lý các tín hiệu kiểm tra và điều khiển quá trình kiểm tra. TAP Controller hoạt động theo một chuỗi trạng thái, cho phép chuyển đổi giữa các chế độ khác nhau như kiểm tra, gỡ lỗi và truyền thông.

2. **Boundary Scan Register**: Đây là một chuỗi các flip-flop được kết nối với các chân của IC. Mỗi flip-flop trong chuỗi này tương ứng với một chân của chip, cho phép kiểm tra trạng thái của các chân mà không cần truy cập trực tiếp vào chúng. Dữ liệu có thể được đưa vào và ra từ các flip-flop này thông qua TAP Controller.

3. **Instruction Register**: Được sử dụng để lưu trữ các lệnh mà TAP Controller sẽ thực hiện. Các lệnh này có thể bao gồm lệnh kiểm tra, lệnh gỡ lỗi hoặc lệnh truyền thông giữa các thiết bị.

4. **Data Register**: Là nơi lưu trữ dữ liệu cần thiết cho quá trình kiểm tra và gỡ lỗi. Dữ liệu này có thể là các giá trị đầu vào hoặc đầu ra mà người dùng muốn kiểm tra.

Nguyên lý hoạt động của **Boundary Scan (JTAG)** bắt đầu từ việc kích hoạt TAP Controller, cho phép nó chuyển sang chế độ kiểm tra. Khi ở chế độ này, người dùng có thể gửi các lệnh thông qua Instruction Register để điều khiển quá trình kiểm tra. Sau đó, dữ liệu có thể được đưa vào hoặc lấy ra từ Boundary Scan Register, cho phép kiểm tra trạng thái của các chân IC mà không cần truy cập vật lý.

Trong quá trình này, các tín hiệu được điều khiển thông qua các đường dẫn kiểm tra riêng biệt, giúp phát hiện và xác định các lỗi trong mạch mà không làm gián đoạn hoạt động của hệ thống. Việc này rất quan trọng trong các ứng dụng yêu cầu độ tin cậy cao, như trong các thiết bị y tế hoặc hàng không.

### 2.1 Các giai đoạn hoạt động
**Boundary Scan (JTAG)** hoạt động qua nhiều giai đoạn, bao gồm:

- **Chế độ Reset**: Bắt đầu với việc đưa TAP Controller về trạng thái khởi động.
- **Chế độ Test-Logic-Reset**: Thiết lập các tín hiệu trong mạch về trạng thái ban đầu.
- **Chế độ Run-Test/Idle**: Cho phép thực hiện các bài kiểm tra mà không làm gián đoạn hoạt động của hệ thống.
- **Chế độ Shift**: Dữ liệu được đưa vào hoặc ra từ các Boundary Scan Register.
- **Chế độ Update**: Cập nhật các giá trị trong mạch dựa trên dữ liệu đã được đưa vào.

## 3. Công nghệ liên quan và So sánh
**Boundary Scan (JTAG)** có nhiều điểm tương đồng và khác biệt với các công nghệ kiểm tra và gỡ lỗi khác trong lĩnh vực điện tử. Một số công nghệ liên quan bao gồm:

- **In-Circuit Testing (ICT)**: ICT là một phương pháp kiểm tra mạch điện tử bằng cách sử dụng các thiết bị kiểm tra chuyên dụng để đo đạc các tín hiệu trên các chân của IC. Mặc dù ICT có khả năng phát hiện các lỗi trong quá trình lắp ráp, nhưng nó yêu cầu truy cập vật lý vào các chân của chip, điều này có thể gây khó khăn trong một số tình huống.

- **Functional Testing**: Đây là phương pháp kiểm tra hoạt động của một hệ thống bằng cách xác định xem nó có thực hiện đúng chức năng hay không. Mặc dù Functional Testing có thể phát hiện các lỗi trong hoạt động của hệ thống, nhưng nó không thể xác định được các lỗi phần cứng cụ thể như **Boundary Scan (JTAG)**.

- **Scan Chain Testing**: Là một phương pháp kiểm tra dựa trên việc kết nối các flip-flop trong một chuỗi để kiểm tra các tín hiệu. Mặc dù phương pháp này có một số điểm tương đồng với **Boundary Scan**, nhưng nó yêu cầu thiết kế mạch phải có cấu trúc cụ thể để thực hiện.

So với các công nghệ khác, **Boundary Scan (JTAG)** có nhiều ưu điểm rõ rệt. Một trong những lợi thế lớn nhất là khả năng thực hiện kiểm tra mà không cần truy cập vật lý vào các chân của chip, giúp tiết kiệm thời gian và chi phí sản xuất. Hơn nữa, **Boundary Scan** cung cấp khả năng gỡ lỗi mạnh mẽ, cho phép các kỹ sư phát hiện và sửa chữa các lỗi trong thiết kế một cách hiệu quả.

Tuy nhiên, **Boundary Scan (JTAG)** cũng có một số nhược điểm. Một trong số đó là yêu cầu phải có phần cứng hỗ trợ và kiến thức chuyên môn để triển khai. Ngoài ra, không phải tất cả các thiết kế đều có thể áp dụng **Boundary Scan**, đặc biệt là những thiết kế không có khả năng hỗ trợ các tín hiệu kiểm tra.

## 4. Tài liệu tham khảo
- IEEE (Institute of Electrical and Electronics Engineers)
- JTAG Technologies
- Boundary Scan Test Association (BSTA)
- Các công ty sản xuất thiết bị kiểm tra điện tử như Keysight Technologies, Tektronix

## 5. Tóm tắt một câu
**Boundary Scan (JTAG)** là một tiêu chuẩn kiểm tra và gỡ lỗi quan trọng trong thiết kế và sản xuất mạch tích hợp, cho phép thực hiện kiểm tra mà không cần truy cập vật lý vào các chân của chip.