# Static Power

## 1. Định nghĩa: **Static Power** là gì?
**Static Power** (công suất tĩnh) là một khái niệm quan trọng trong thiết kế mạch số, đặc biệt trong các hệ thống VLSI (Very Large Scale Integration). Nó được định nghĩa là công suất tiêu thụ của một mạch khi không có thay đổi trạng thái, tức là khi các tín hiệu không thay đổi. Trong các mạch số, Static Power chủ yếu phát sinh từ các thành phần như MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor) trong trạng thái tắt (off state) và do hiện tượng rò rỉ điện. 

Công suất tĩnh có vai trò quan trọng trong việc xác định hiệu suất năng lượng của các thiết bị điện tử, đặc biệt là trong các ứng dụng di động và IoT (Internet of Things), nơi mà việc tiết kiệm năng lượng là rất cần thiết. Khi các thiết bị trở nên nhỏ hơn và tích hợp nhiều chức năng hơn, Static Power trở thành một yếu tố quan trọng trong việc thiết kế và tối ưu hóa hệ thống. 

Thực tế, Static Power có thể chiếm một phần lớn trong tổng công suất tiêu thụ của một hệ thống, đặc biệt là trong các mạch tích hợp lớn. Do đó, việc hiểu rõ về Static Power giúp các kỹ sư thiết kế các giải pháp hiệu quả hơn, giảm thiểu tiêu thụ năng lượng và kéo dài tuổi thọ pin trong các thiết bị di động.

## 2. Thành phần và Nguyên lý hoạt động
Static Power chủ yếu bao gồm hai thành phần chính: công suất rò rỉ và công suất tĩnh. 

### 2.1 Công suất rò rỉ
Công suất rò rỉ là một phần không thể tránh khỏi trong thiết kế mạch số, đặc biệt là khi công nghệ chế tạo các transistor ngày càng nhỏ. Trong các transistor MOSFET, công suất rò rỉ xảy ra do các dòng điện nhỏ vẫn chảy qua các transistor khi chúng ở trạng thái tắt. Có nhiều loại rò rỉ khác nhau, bao gồm rò rỉ subthreshold, rò rỉ gate oxide và rò rỉ junction. 

- **Rò rỉ subthreshold**: Xảy ra khi điện áp gate thấp hơn điện áp ngưỡng, nhưng vẫn đủ để cho phép một dòng điện nhỏ chảy qua.
- **Rò rỉ gate oxide**: Xuất hiện do các electron có thể xuyên qua lớp oxit giữa gate và channel của transistor.
- **Rò rỉ junction**: Liên quan đến các dòng điện chảy qua các tiếp điểm p-n trong transistor.

### 2.2 Công suất tĩnh
Công suất tĩnh thường được tính toán dựa trên các thông số thiết kế của mạch, bao gồm kích thước transistor, điện áp cung cấp và tần suất hoạt động. Khi thiết kế các mạch VLSI, các kỹ sư thường phải cân nhắc giữa kích thước transistor và mức tiêu thụ công suất tĩnh. Việc giảm kích thước transistor có thể dẫn đến tăng cường công suất rò rỉ, do đó cần có sự cân bằng hợp lý.

### 2.3 Nguyên lý hoạt động
Static Power hoạt động dựa trên nguyên lý rằng khi một transistor ở trạng thái tắt, nó vẫn có thể cho phép một dòng điện nhỏ chảy qua. Điều này có nghĩa là ngay cả khi không có tín hiệu thay đổi, mạch vẫn tiêu thụ một lượng công suất nhất định. Các yếu tố ảnh hưởng đến Static Power bao gồm điện áp cung cấp, kích thước transistor, và công nghệ chế tạo. 

Việc giảm thiểu Static Power có thể đạt được thông qua các phương pháp thiết kế như sử dụng transistor với ngưỡng thấp hơn, tối ưu hóa kích thước transistor, và áp dụng các kỹ thuật chế tạo tiên tiến để giảm thiểu các hiện tượng rò rỉ.

## 3. Công nghệ liên quan và So sánh
Khi so sánh Static Power với các công nghệ liên quan khác, như Dynamic Power, có thể thấy những điểm khác biệt rõ rệt. Dynamic Power chủ yếu phát sinh từ sự chuyển đổi trạng thái của các tín hiệu trong mạch, trong khi Static Power xảy ra ngay cả khi không có chuyển đổi nào. 

### 3.1 So sánh với Dynamic Power
- **Đặc điểm**: Dynamic Power phụ thuộc vào tần suất hoạt động và điện tích chuyển đổi, trong khi Static Power chủ yếu phụ thuộc vào điện áp và các đặc tính của transistor.
- **Ưu điểm**: Static Power thường ổn định hơn và dễ dự đoán trong các thiết kế, trong khi Dynamic Power có thể thay đổi tùy thuộc vào hoạt động của hệ thống.
- **Nhược điểm**: Static Power có thể làm giảm hiệu suất năng lượng tổng thể của các thiết bị, đặc biệt trong các ứng dụng yêu cầu hoạt động liên tục.

### 3.2 Ví dụ thực tế
Trong các thiết bị di động như smartphone, Static Power chiếm một phần lớn trong tổng công suất tiêu thụ, đặc biệt khi thiết bị ở chế độ chờ. Việc tối ưu hóa Static Power trở thành một yếu tố quan trọng trong việc kéo dài tuổi thọ pin. Các nhà sản xuất chip như Intel và AMD đã đầu tư rất nhiều vào việc giảm thiểu Static Power trong các sản phẩm của họ, thông qua việc cải tiến công nghệ chế tạo và thiết kế mạch.

## 4. Tài liệu tham khảo
- IEEE (Institute of Electrical and Electronics Engineers)
- ACM (Association for Computing Machinery)
- Các công ty như Intel, AMD, và TSMC có liên quan đến nghiên cứu và phát triển Static Power trong các sản phẩm của họ.

## 5. Tóm tắt một câu
Static Power là công suất tiêu thụ của mạch số khi không có thay đổi trạng thái, chủ yếu phát sinh từ hiện tượng rò rỉ trong các transistor, và đóng vai trò quan trọng trong việc thiết kế và tối ưu hóa hiệu suất năng lượng của các hệ thống VLSI.