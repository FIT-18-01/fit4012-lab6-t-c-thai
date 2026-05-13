# Report 1 page - Lab 6 AES-CBC Socket

## Thông tin nhóm

- Thành viên 1: Phạm Văn Chung
- Thành viên 2: Vũ Hồng Sơn


## Mục tiêu

TODO_STUDENT: Viết 4-6 dòng mô tả mục tiêu của bài lab: gửi/nhận dữ liệu qua socket, mã hóa AES-CBC, tách kênh khóa và kênh dữ liệu, kiểm thử và phân tích điểm yếu bảo mật.

## Phân công thực hiện

TODO_STUDENT: Mô tả ai phụ trách sender, ai phụ trách receiver, ai phụ trách test/log/threat model, và phần làm chung.

## Cách làm

Nhóm sử dụng Python socket để tạo kết nối giữa Sender và Receiver. Dữ liệu trước khi gửi được mã hóa bằng thuật toán AES-CBC kết hợp với PKCS#7 padding để đảm bảo dữ liệu phù hợp kích thước block. Hệ thống sử dụng hai kênh riêng biệt: key channel dùng để truyền khóa AES và data channel dùng để truyền dữ liệu đã mã hóa. Ngoài ra, chương trình còn sử dụng length header để xác định kích thước dữ liệu trước khi nhận nhằm tránh lỗi thiếu hoặc dư dữ liệu trong quá trình truyền.

## Kết quả

Chương trình gửi và nhận dữ liệu thành công giữa hai socket. Dữ liệu sau khi giải mã tại Receiver khớp với dữ liệu ban đầu từ Sender. Các log minh chứng cho thấy quá trình mã hóa, gửi dữ liệu và giải mã hoạt động ổn định. Nhóm cũng thực hiện các test quan trọng như test truyền dữ liệu đúng, test sai khóa và negative test tamper/flip 1 byte để kiểm tra khả năng phát hiện dữ liệu bị thay đổi.

## Kết luận

Qua bài lab, nhóm hiểu rõ hơn về cách hoạt động của AES-CBC và cơ chế truyền dữ liệu an toàn qua socket. Việc tách key channel và data channel giúp nâng cao tính bảo mật cho hệ thống. Ngoài ra, nhóm nhận thấy rằng nếu dữ liệu bị thay đổi trong quá trình truyền thì hệ thống cần có cơ chế kiểm tra tính toàn vẹn để phát hiện lỗi. Bài lab giúp củng cố kỹ năng lập trình mạng, xử lý mã hóa và tư duy phân tích bảo mật trong thực tế.