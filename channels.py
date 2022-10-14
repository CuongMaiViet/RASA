from utters import Utters


class Channels:
    def __init__(self, user_title, user_name) -> None:
        self.user_title = user_title
        self.utter = Utters(user_title, user_name)
        self.capTitle = self.utter.capTitle
        self.bot_name = self.utter.bot_name

    def ChannelSupportCW(self):
        utter = self.utter
        title = self.user_title
        capTitle = self.capTitle
        bot_name = self.bot_name

        return {
            "chào_mừng": {
                "message": utter.chào_mừng(),
                "message_type": "full_of_text",
                "payload": [
                    {"title": f"{capTitle} muốn nói chuyện với chuyên viên tư vấn giải pháp",
                     "value": '/gặp_chuyên_viên_tư_vấn_giải_pháp'},
                    {"title": f"{capTitle} đang là khách hàng của bên công ty {bot_name}",
                     "value": '/khách_hàng_hiện_hữu'},
                    {"title": f"{capTitle} đang tìm hiểu thông tin",
                     "value": '/tìm_kiếm_thông_tin'},
                    {"title": f"{capTitle} muốn trở thành đối tác, đại lý của ePacific Telecom",
                     "value": '/đăng_ký_làm_đại_lý'}
                ]
            },
            "xem_menu": {
                "message": utter.xem_menu(),
                "message_type": "full_of_text",
                "payload": [
                    {"title": f"{capTitle} muốn nói chuyện với chuyên viên tư vấn giải pháp",
                     "value": '/gặp_chuyên_viên_tư_vấn_giải_pháp'},
                    {"title": f"{capTitle} đang là khách hàng của bên công ty {bot_name}",
                     "value": '/khách_hàng_hiện_hữu'},
                    {"title": f"{capTitle} đang tìm hiểu thông tin",
                     "value": '/tìm_kiếm_thông_tin'},
                    {"title": f"{capTitle} muốn trở thành đối tác, đại lý của ePacific Telecom",
                     "value": '/đăng_ký_làm_đại_lý'}
                ]
            },
            "cung_cấp_tên": {
                "message": utter.chào_mừng(),
                "message_type": "full_of_text",
                "payload": [
                    {"title": f"{capTitle} muốn nói chuyện với chuyên viên tư vấn giải pháp",
                     "value": '/gặp_chuyên_viên_tư_vấn_giải_pháp'},
                    {"title": f"{capTitle} đang là khách hàng của bên công ty {bot_name}",
                     "value": '/khách_hàng_hiện_hữu'},
                    {"title": f"{capTitle} đang tìm hiểu thông tin",
                     "value": '/tìm_kiếm_thông_tin'},
                    {"title": f"{capTitle} muốn trở thành đối tác, đại lý của ePacific Telecom",
                     "value": '/đăng_ký_làm_đại_lý'}
                ]
            },
            "gặp_chuyên_viên_tư_vấn_giải_pháp": {
                "message": utter.gặp_chuyên_viên_tư_vấn_giải_pháp(),
                "message_type": "full_of_text",
                "payload": [
                    {"title": f"{capTitle} đang cần tư vấn một hệ thống Trung tâm liên lạc cho doanh nghiệp của mình",
                     "value": '/tư_vấn_hệ_thống_trung_tâm_liên_lạc_cho_doanh_nghiệp'},
                    {"title": f"{capTitle} đang cần tư vấn một hệ thống trung tâm liên lạc cho khách hàng của công ty {title}",
                     "value": '/tư_vấn_hệ_thống_trung_tâm_liên_lạc_cho_khách_hàng'},
                    {"title": f"{capTitle} đang đánh giá các sản phẩm khác của ePacific (ví dụ như là tổng đài CCALL, softphone, AI, v.v.)",
                     "value": '/đánh_giá_các_sản_phẩm_khác_của_ePacific'}
                ]
            },
            "cung_cấp_email": {
                "message": utter.gặp_chuyên_viên_tư_vấn_giải_pháp(),
                "message_type": "full_of_text",
                "payload": [
                    {"title": f"{capTitle} đang cần tư vấn một hệ thống Trung tâm liên lạc cho doanh nghiệp của mình",
                     "value": '/tư_vấn_hệ_thống_trung_tâm_liên_lạc_cho_doanh_nghiệp'},
                    {"title": f"{capTitle} đang cần tư vấn một hệ thống trung tâm liên lạc cho khách hàng của công ty {title}",
                     "value": '/tư_vấn_hệ_thống_trung_tâm_liên_lạc_cho_khách_hàng'},
                    {"title": f"{capTitle} đang đánh giá các sản phẩm khác của ePacific (ví dụ như là tổng đài CCALL, softphone, AI, v.v.)",
                     "value": '/đánh_giá_các_sản_phẩm_khác_của_ePacific'}
                ]
            },
            "khách_hàng_hiện_hữu": {
                "message": utter.khách_hàng_hiện_hữu(),
                "message_type": "full_of_text",
                "payload": [
                    {"title": f"{capTitle} muốn trò chuyện với một chuyên gia bán hàng về sản phẩm",
                     "value": '/gặp_chuyên_viên_tư_vấn_giải_pháp'},
                    {"title": f"{capTitle} cần hỗ trợ kỹ thuật về sản phẩm mà bên tôi đang sử dụng",
                     "value": '/hỗ_trợ_kỹ_thuật_sử_dụng'},
                    {"title": f"{capTitle} có câu hỏi về xử lý đơn hàng, hoá đơn, bảo hành, v.v.",
                     "value": '/xử_lý_đơn_hàng_hoa_đơn'},
                ]
            },
            "xử_lý_đơn_hàng_hoa_đơn": {
                "message": utter.xử_lý_đơn_hàng_hóa_đơn(),
                "message_type": "full_of_text",
                "payload": [
                    {"title": f"Xử lý đơn hàng",
                     "value": '/xử_lý_đơn_hàng'},
                    {"title": f"Xử lý hóa đơn",
                     "value": '/xử_lý_hóa_đơn'}
                ]
            },
            "tìm_kiếm_thông_tin": {
                "message": utter.tìm_kiếm_thông_tin(),
                "message_type": "cards",
                "payload": [{
                    "media_url": "https://ml6j2y9i2dsk.i.optimole.com/dQjH4ko-Ho71wJ1Q/w:auto/h:auto/q:mauto/https://epacific.com.vn/wp-content/uploads/2020/12/ePacific-Telecom-eTouch.png",
                    "title": "Tìm kiếm thông tin",
                    "description": f"đây là đường link",
                    "actions": [
                        {
                            "text": "Khách hàng",
                            "type": "link",
                            "uri": "https://epacific.com.vn/smart-assist-chuc-nang-hieu-qua-danh-cho-linh-vuc-dich-vu-khach-hang-2/"
                        },
                        {
                            "text": "Giao dịch viên",
                            "type": "link",
                            "uri": "https://epacific.com.vn/tro-ly-nhan-vien-ai/"
                        },
                        {
                            "text": "Nhân viên",
                            "type": "link",
                            "uri": "https://epacific.com.vn/ho-tro-it/"
                        },
                    ]
                }]
            },
            "đăng_ký_làm_đại_lý": {
                "message": utter.đăng_ký_làm_đại_lý(),
                "message_type": "no_payload"
            },
            "gặp_tư_vấn_viên": {
                "message": utter.gặp_tư_vấn_viên(),
                "message_type": "no_payload"
            }
        }