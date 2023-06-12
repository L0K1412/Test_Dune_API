# API Overview

Điểm mạnh:
- Không giới hạn thời gian
- Không giới hạn kết quả
- Data được cập nhật gần như bằng thời gian thực
- Thời gian chạy khá nhanh
- Số lượng credit tiêu tốn mỗi lần chạy query là cố định => dễ kiểm soát + tính toán

Điểm yếu:
- Bắt buộc phải tạo sẵn query trên dune để lấy id query để chạy
- Không chỉnh sửa được code query bằng python

1 số điểm cần chú ý:
- Có 2500 credits/ 1 tháng
- Có 2 kiểu chạy query = api: medium và large
- Medium: tốn 10 credits 1 lần chạy, chạy nhanh hơn free
=> nếu mà chạy 1 câu lệnh = medium thì có thể chạy tối đa 1 lần/ 3 tiếng/ 1 tháng
- Large: tốn 20 credits 1 lần chạy, chạy nhanh hơn large
- Nếu chạy query có param nhưng không điền param thì nó sẽ chạy với default params được set sẵn trong query trên dune
