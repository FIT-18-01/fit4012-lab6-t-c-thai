# Peer Review Response

## Peer feedback summary

Nhóm đã review các phần sender, receiver, AES-CBC, logging và test.

## Issues found

- Cần xử lý retry khi socket chưa sẵn sàng.
- Cần bổ sung file peer-review-response.md để đúng submission contract.
- Cần kiểm tra timing giữa key channel và data channel.

## Improvements applied

- Đã thêm retry logic cho sender socket connection.
- Đã thêm delay ngắn giữa key channel và data channel.
- Đã bổ sung đầy đủ file yêu cầu của repo.