# Memory Built In Self Test (MBIST)

## 1. Định nghĩa: **Memory Built In Self Test (MBIST)** là gì?
**Memory Built In Self Test (MBIST)** là một kỹ thuật kiểm tra tự động được tích hợp trong các hệ thống nhớ để xác định và phát hiện lỗi trong các mô-đun nhớ. Kỹ thuật này rất quan trọng trong thiết kế mạch số (Digital Circuit Design) vì nó cho phép việc kiểm tra và xác minh tính toàn vẹn của dữ liệu mà không cần đến thiết bị kiểm tra bên ngoài. MBIST thường được sử dụng trong các ứng dụng VLSI (Very Large Scale Integration) nơi mà việc kiểm tra các mô-đun nhớ trở nên cần thiết do yêu cầu cao về độ tin cậy và hiệu suất.

MBIST hoạt động bằng cách tạo ra các mẫu dữ liệu kiểm tra nhất định, sau đó ghi chúng vào mô-đun nhớ và đọc lại để so sánh với các mẫu ban đầu. Nếu có sự khác biệt, điều đó cho thấy có lỗi trong mô-đun nhớ. Kỹ thuật này không chỉ giúp phát hiện lỗi mà còn cung cấp thông tin về loại lỗi, từ đó giúp cho việc sửa chữa và cải thiện thiết kế. 

Một trong những điểm mạnh của MBIST là khả năng thực hiện kiểm tra trong quá trình sản xuất và trong suốt vòng đời của thiết bị, điều này giúp giảm thiểu chi phí bảo trì và tăng cường độ tin cậy. MBIST cũng cho phép kiểm tra các mô-đun nhớ với tốc độ cao, điều này rất quan trọng trong các ứng dụng yêu cầu thời gian thực, như trong các hệ thống nhúng và viễn thông.

## 2. Thành phần và nguyên lý hoạt động
Memory Built In Self Test (MBIST) bao gồm nhiều thành phần chính và hoạt động theo một chu trình rõ ràng để thực hiện kiểm tra. Các thành phần chính bao gồm:

1. **Test Pattern Generator (TPG)**: Đây là thành phần tạo ra các mẫu dữ liệu kiểm tra. TPG có thể sử dụng các thuật toán như March Test hoặc Checkerboard Test để tạo ra các mẫu kiểm tra phù hợp với loại lỗi mà mô-đun nhớ có thể gặp phải.

2. **Memory Under Test (MUT)**: Đây là mô-đun nhớ thực tế mà MBIST sẽ kiểm tra. MUT có thể là SRAM, DRAM hoặc Flash tùy thuộc vào ứng dụng.

3. **Response Analyzer (RA)**: Thành phần này chịu trách nhiệm so sánh dữ liệu đọc được từ MUT với các mẫu kiểm tra ban đầu. Nếu có sự không khớp, RA sẽ ghi nhận lỗi và cung cấp thông tin cho các bước xử lý tiếp theo.

4. **Control Logic**: Đây là phần điều khiển toàn bộ quy trình kiểm tra, bao gồm việc khởi động TPG, quản lý dữ liệu từ MUT và điều phối RA. Control Logic thường được lập trình để thực hiện các chu trình kiểm tra khác nhau và có thể được điều chỉnh cho phù hợp với các yêu cầu cụ thể của thiết kế.

Nguyên lý hoạt động của MBIST diễn ra qua các bước sau:

- **Khởi động**: Control Logic khởi động quy trình kiểm tra bằng cách kích hoạt TPG để tạo ra các mẫu kiểm tra.
- **Ghi dữ liệu**: Các mẫu này được ghi vào MUT.
- **Đọc dữ liệu**: Sau khi ghi xong, dữ liệu được đọc lại từ MUT.
- **Phân tích phản hồi**: RA so sánh dữ liệu đọc được với các mẫu ban đầu để xác định có lỗi hay không.
- **Báo cáo kết quả**: Nếu phát hiện lỗi, MBIST sẽ ghi lại thông tin chi tiết về lỗi để phục vụ cho việc sửa chữa hoặc cải thiện thiết kế trong tương lai.

### 2.1 Các phương pháp triển khai MBIST
Có nhiều phương pháp triển khai MBIST khác nhau, bao gồm:

- **MBIST tích hợp**: Trong phương pháp này, MBIST được tích hợp trực tiếp vào mạch thiết kế, cho phép kiểm tra dễ dàng trong suốt quá trình sản xuất và sau khi thiết bị đã được đưa vào sử dụng.
- **MBIST ngoài**: Đây là phương pháp sử dụng các thiết bị kiểm tra bên ngoài để thực hiện kiểm tra. Phương pháp này thường phức tạp hơn và có thể tốn kém hơn do yêu cầu thiết bị bổ sung.

## 3. Công nghệ liên quan và so sánh
Memory Built In Self Test (MBIST) có thể được so sánh với một số công nghệ và phương pháp kiểm tra khác như:

- **Boundary Scan**: Đây là một kỹ thuật kiểm tra mạch tích hợp cho phép kiểm tra các tín hiệu đầu vào và đầu ra mà không cần truy cập vật lý vào các chân của chip. Trong khi MBIST tập trung vào kiểm tra mô-đun nhớ, Boundary Scan chủ yếu được sử dụng cho kiểm tra các mạch số khác.

- **Built-In Self Test (BIST)**: Đây là một khái niệm rộng hơn, trong đó MBIST là một ứng dụng cụ thể. BIST có thể áp dụng cho nhiều loại thành phần khác nhau, không chỉ giới hạn ở mô-đun nhớ. So với MBIST, BIST thường yêu cầu nhiều tài nguyên hơn và có thể phức tạp hơn trong việc triển khai.

### So sánh tính năng
- **Ưu điểm của MBIST**: MBIST cung cấp khả năng kiểm tra tự động, giảm thiểu thời gian và chi phí kiểm tra, đồng thời tăng cường độ tin cậy của các mô-đun nhớ. Nó cũng có khả năng phát hiện lỗi nhanh chóng và hiệu quả, điều này rất quan trọng trong sản xuất hàng loạt.

- **Nhược điểm của MBIST**: Một số nhược điểm bao gồm việc yêu cầu không gian trên chip cho các thành phần MBIST, có thể làm tăng chi phí sản xuất. Ngoài ra, MBIST có thể không phát hiện được tất cả các loại lỗi, đặc biệt là những lỗi liên quan đến điều kiện hoạt động thực tế.

## 4. Tài liệu tham khảo
- IEEE (Institute of Electrical and Electronics Engineers)
- ACM (Association for Computing Machinery)
- Các công ty như Synopsys, Mentor Graphics và Cadence Design Systems, chuyên cung cấp công cụ và giải pháp cho MBIST.

## 5. Tóm tắt một dòng
Memory Built In Self Test (MBIST) là một kỹ thuật kiểm tra tự động tích hợp trong các mô-đun nhớ, cho phép phát hiện lỗi một cách hiệu quả và tiết kiệm chi phí trong thiết kế mạch số.