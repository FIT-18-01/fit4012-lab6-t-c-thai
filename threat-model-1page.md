# Threat Model - Lab 6 AES-CBC Socket

## Thông tin nhóm

- Thành viên 1: Phạm Văn Chung
- Thành viên 2: Vũ Hồng Sơn


## Assets

TODO_STUDENT: Liệt kê tài sản cần bảo vệ, ví dụ plaintext, AES key, IV, ciphertext, file đầu vào, file đầu ra và log.

## Attacker model

TODO_STUDENT: Mô tả đối tượng tấn công có thể nghe lén mạng LAN, bắt gói tin, sửa ciphertext, replay packet hoặc đọc log.

## Threats

TODO_STUDENT: Nêu ít nhất 3 mối đe dọa cụ thể, ví dụ:
- Key disclosure do key/IV gửi plaintext.
- Tampering do ciphertext bị sửa.
- Replay attack do packet cũ bị gửi lại.
- Log leakage do key bị ghi vào log.
- No authentication do Receiver không xác thực Sender.

## Mitigations

- Không truyền AES key dưới dạng plaintext trong hệ thống thực tế.
- Sử dụng TLS hoặc cơ chế trao đổi khóa an toàn để bảo vệ key channel.
- Dùng AES-GCM hoặc thêm HMAC để kiểm tra tính toàn vẹn và xác thực dữ liệu.
- Không ghi key thật hoặc thông tin nhạy cảm vào log trong môi trường production.
- Thêm nonce hoặc timestamp để giảm nguy cơ replay attack.
- Thêm cơ chế xác thực Sender trước khi Receiver chấp nhận dữ liệu.

## Residual risks

Hệ thống vẫn còn một số rủi ro vì key channel chỉ mang tính mô phỏng và chưa sử dụng TLS thực sự. Ngoài ra, chương trình chưa có cơ chế xác thực đầy đủ giữa Sender và Receiver, đồng thời replay attack vẫn chưa được ngăn chặn hoàn toàn trong mọi trường hợp.