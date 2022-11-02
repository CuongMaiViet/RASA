import secrets
from functions import cap, get_current_period, read_json


class Utters:
    def __init__(self, user_title, user_name) -> None:
        self.user_title = user_title
        self.user_name = user_name
        self.bot_name = "Mai"

        self.capTitle = cap(user_title)
        self.period = get_current_period()
        self.emojis = read_json("emojis.json")

    def chào_mừng(self):
        return secrets.choice([
            [f"Chào buổi {self.period} nha {self.user_title} {self.user_name} {self.emojis.get('beaming_face_with_smiling_eyes')}",
             f"{self.capTitle} giúp {self.bot_name} chọn một trong các mục dưới đây"],
            [f"Buổi {self.period} tốt lành nha {self.user_title} {self.user_name} {self.emojis.get('beaming_face_with_smiling_eyes')}",
             f"{self.capTitle} vui lòng chọn một trong các mục dưới đây giúp {self.bot_name}"],
        ])

    def xem_menu(self):
        return secrets.choice([
            [f"Vâng, menu của {self.user_title} đây ạ",
                f"{self.capTitle} giúp {self.bot_name} chọn một trong các mục dưới đây"],
            [f"Menu {self.user_title} yêu cầu đây",
                f"{self.capTitle} vui lòng chọn một trong các mục dưới đây giúp {self.bot_name}"],
        ])

    def gặp_chuyên_viên_tư_vấn_giải_pháp(self):
        return secrets.choice([
            ["Tuyệt vời!",
                f"Nhưng mà trước khi em chuyển máy cho {self.user_title} tới chuyên viên tư vấn giải pháp, hãy cho {self.bot_name} biết thêm một chút về nhu cầu của {self.user_title}"],
            [f"Vâng thưa {self.user_title}",
                f"Nhưng mà trước khi {self.bot_name} chuyển máy cho {self.user_title} tới chuyên viên tư vấn giải pháp, hãy cho em biết thêm một chút về nhu cầu của {self.user_title}"]
        ])

    def khách_hàng_hiện_hữu(self):
        return secrets.choice([
            f"Để em có thể hỗ trợ {self.user_title} tốt nhất, điều nào sau đây mô tả chính xác nhất yêu cầu của {self.user_title} ạ",
            [f"Vâng {self.user_title}",
                f"Nhưng mà {self.user_title} vui lòng mô tả chính xác nhất yêu cầu để em có thể hỗ trợ {self.user_title} tốt nhất ạ"]
        ])

    def xử_lý_đơn_hàng_hóa_đơn(self):
        return secrets.choice([
            [f"Vâng {self.user_title}",
                f"Trước khi Mai chuyển tiếp tới chuyên viên phụ trách, có phải {self.user_title} mong muốn:"]
        ])

    def tìm_kiếm_thông_tin(self):
        return secrets.choice([
            [f"Vâng thưa {self.user_title}",
                f"{self.capTitle} vui lòng nhấp vào liên kết tới thông tin chi tiết về các giải pháp cải thiện trải nghiệm theo từng kiểu đối tượng, dưới đây:"]
        ])

    def xin_số_điện_thoại_chăm_sóc_khách_hàng(self):
        return secrets.choice([
            f"Số chăm sóc KH bên em là 1900-0038 ạ",
            f"1900-0038 ạ",
            f"Dạ gọi tới 1900-0038 là được ạ",
        ])

    def đăng_ký_làm_đại_lý(self):
        return secrets.choice([
            f"Để tiện liên lạc {self.user_title} vui lòng cho {self.bot_name} biết thông tin sau:"
        ])

    def gặp_tư_vấn_viên(self):
        response = secrets.choice([
            f"Vâng. {self.capTitle} chờ chút. {self.bot_name} sẽ chuyển tiếp yêu cầu tới chuyên viên tư vấn ngay đây ạ.",
            f"{self.bot_name} đang chuyển máy đến chuyên viên tư vấn.",
        ])

        return response + " Vui lòng đợi trong giây lát..."
