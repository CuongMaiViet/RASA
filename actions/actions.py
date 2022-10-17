from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

from responses import Responses
from User import User
from functions import check_agent_availability, check_name, is_alphabet, is_valid_site, is_valid_phone_number, is_valid_email, read_json

MALE = ["nam", "male", "anh"]
FEMALE = ["nữ", "female", "chị"]
LEGAL_CHANNELS = ["ChannelWebWidget", "ChannelApi", "ChannelTelegram"]

URL = "https://ccai.epacific.net/api/v1/accounts/1"
TOKEN = "78ARRSX2ofwSwVJJGivJiBTP"


class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # period = MULTIUSES.get_current_period()
        user_name = tracker.get_slot("user_name")
        user_title = tracker.get_slot("user_title") or "quý khách"

        if user_name is None:
            dispatcher.utter_message(
                text=f"Xin chào! Em là Mai, trợ lý số của công ty")
            dispatcher.utter_message(
                text=f"Trước khi em có thể hỗ trợ {user_title}, cho em xin một số thông tin cơ bản của {user_title} để tiện xưng hô ạ")

        # elif user_name is not None:
        #     dispatcher.utter_message(
        #         text=f"Chào buổi {period} nha {user_title} {user_name}!")

        return


class ActionGreet(Action):
    def name(self) -> Text:
        return "action_explain_fill_form"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        intent = tracker.latest_message["intent"]["name"]
        user = User(tracker)
        user_title = user.get_title()
        # user_name = user.get_name()
        user_email = tracker.get_slot("user_email")
        user_phone = tracker.get_slot("user_phone")
        user_website = tracker.get_slot("user_website")

        emoji = read_json("emojis.json")

        if intent == "xử_lý_đơn_hàng" or intent == "xử_lý_hóa_đơn" or intent == "hỗ_trợ_kỹ_thuật_sử_dụng":
            if user_email is not None and user_phone is not None:
                return

            if intent == "hỗ_trợ_kỹ_thuật_sử_dụng":
                dispatcher.utter_message(
                    text=f"Trước khi Mai chuyển tiếp cho chuyên viên hỗ trợ, mong {user_title} cung cấp một số thông tin liên lạc cần thiết!!!")
            else:
                dispatcher.utter_message(
                    text=f"Vui lòng cho em xin một số thông tin cần thiết để xử lý yêu cầu của {user_title} ạ!")

            if user_email is None and user_phone is not None:
                dispatcher.utter_message(
                    text=f"Em có số điện thoại của {user_title} rồi, còn lại email nữa")
                return
            elif user_email is not None and user_phone is None:
                dispatcher.utter_message(
                    text=f"Em có email của {user_title} rồi, còn lại số điện thoại nữa")
                return
            return

        if intent == "đăng_ký_làm_đại_lý":
            if user_email is not None and user_phone is not None and user_website is not None:
                return

            dispatcher.utter_message(
                text=f"Để tiện liên lạc {user_title} vui lòng cho em biết một số thông tin sau")
            return

        if intent == "gặp_chuyên_viên_tư_vấn_giải_pháp":
            if user_email is not None:
                return

            dispatcher.utter_message(
                text=f"Vâng chắc chắn rồi ạ")
            dispatcher.utter_message(
                text=f"Nhưng mà {user_title}, em bảo cái này tí")
            dispatcher.utter_message(
                text=f"Sếp bảo em phải có email của khách thì mới được chuyển tiếp cho chuyên viên tư vấn á {emoji.get('pensive_face')}")
            dispatcher.utter_message(
                text=f"Nên {user_title} à {emoji.get('pleading_face')}")
            return

        return


class ActionMain(Action):

    def name(self) -> Text:
        return "action_main"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        channel = "ChannelWebWidget"
        # channel = tracker.get_slot("channel")

        if channel is None:
            print("channel is None")
            dispatcher.utter_message(text="Không tìm thấy kênh nào cả")
            return

        if channel not in LEGAL_CHANNELS:
            print("illegal channel")
            dispatcher.utter_message(text="Kênh không được hỗ trợ AI")
            return

        intent = tracker.latest_message["intent"]["name"]
        user = User(tracker)
        user_title = user.get_title()
        user_name = user.get_name()

        responses = Responses(channel, user_title, user_name)
        if intent not in list(responses.get_channel_data().keys()):
            dispatcher.utter_message(
                text=f"Không xác định được mong muốn của {user_title}. Có thể do em chưa được dạy cái này. Mong {user_title} có thể diễn đạt lại")
            return
        responses.get_bot_responses(dispatcher, intent)

        return []


class ActionHandoff(Action):

    def name(self) -> Text:
        return "action_handoff"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        is_agent_available = check_agent_availability(f"{URL}/agents", TOKEN)
        intent = tracker.latest_message["intent"]["name"]

        user = User(tracker)
        user_title = user.get_title()
        user_name = user.get_name()

        # user_email = tracker.get_slot("user_email")
        # user_phone = tracker.get_slot("user_phone")
        # user_website = tracker.get_slot("user_website")
        # print(user_email)
        # print(user_phone)
        # print(user_website)

        if intent.startswith("cung_cấp"):
            dispatcher.utter_message(
                text=f"Cảm ơn {user_title} đã cung cấp thông tin")
            dispatcher.utter_message(
                text=f"Bây giờ Mai sẽ tìm xem có chuyên viên nào online không thì chuyển máy cho {user_title} nha")
            dispatcher.utter_message(text=f"Đợi Mai tí")
        else:
            dispatcher.utter_message(
                text=f"Okay giờ {user_title} đợi Mai tìm xem có chuyên viên nào trực không thì chuyển máy cho {user_title} nha")
            dispatcher.utter_message(text=f"Đợi Mai chút xíu")

        if is_agent_available is False:
            dispatcher.utter_message(
                text=f"Rất tiết hiện Mai chưa tìm được chuyên viên nào online để thảo luận với {user_title}. Lát nữa sẽ có người liên hệ lại với {user_title} {user_name} nhé.")
            dispatcher.utter_message(
                text=f"Trong lúc chờ đợi, {user_title} cần hỗ trợ thêm gì nữa không? Hoặc {user_title} có thể xem thông tin trên web <https://epacific.com.vn/>")
            return

        dispatcher.utter_message(text=f"Okay, Mai tìm thấy rồi")
        dispatcher.utter_message(
            text=f"Mai đang chuyển tiếp cuộc hội thoại này tới chuyên viên nha. Vui lòng đợi trong giây lát...")
        return []


class ValidateUserInformationForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_user_information_form"

    async def validate_user_title(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        gender = slot_value.lower()
        if gender not in MALE and gender not in FEMALE:
            dispatcher.utter_message(
                text="Giới tính này không đúng. Quý khách vui lòng cung cấp đúng giới tính")
            return {"user_title": None}

        title = "anh"
        if gender in FEMALE:
            title = "chị"

        # dispatcher.utter_message(text=f"Cảm ơn {title}, em sẽ ghi nhớ")
        return {"user_title": title}

    async def validate_user_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        user_title = tracker.get_slot("user_title")

        valid = is_alphabet(slot_value)
        if not valid:
            dispatcher.utter_message(
                text=f"Tên {user_title} không nên chứa số hay ký tự đặc biệt vì nó không phải là một cái tên đúng @@")
            return {"user_name": None}

        checked_name = check_name(slot_value)
        if checked_name is None:
            dispatcher.utter_message(
                text=f"Em tìm trong từ điển không thấy tên của {user_title}. Vui lòng cung cấp lại")
            return {"user_name": None}

        # dispatcher.utter_message(text=f"Dạ vâng, em chào {user_title} {slot_value}")
        return {"user_name": checked_name.get("first_name")}


class ValidateEmailPhoneWebsiteForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_email_phone_website_form"

    async def validate_user_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if is_valid_email(slot_value) == "UNDELIVERABLE":
            dispatcher.utter_message(
                text=f"Em kiểm tra thấy email '{slot_value}' không tồn tại hoặc không thể tương tác. Vui lòng nhập lại")
            return {"user_email": None}

        return {"user_email": slot_value}

    async def validate_user_phone(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        valid = is_valid_phone_number(slot_value)
        if valid is False or valid is None:
            dispatcher.utter_message(
                text=f"Em kiểm tra thấy số điên thoại '{slot_value}' không hợp lệ. Vui lòng nhập lại")
            return {"user_phone": None}

        return {"user_phone": slot_value}

    async def validate_user_website(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        valid = is_valid_site(slot_value)
        if valid == "Site is up.":
            return {"user_website": slot_value}
        elif valid == "Unable to reach the URL.":
            dispatcher.utter_message(text=f"Em kiểm và thấy rằng website '{slot_value}' không tồn tại. Vui lòng nhập lại")
            return {"user_website": None}
        elif valid == "Site is down":
            dispatcher.utter_message(
                text=f"Em kiểm và thấy rằng website '{slot_value}' đã bị gỡ hoặc không khả dụng ở thời điểm hiện tại. Vui lòng nhập lại")
            return {"user_website": None}


class ValidateEmailForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_email_form"

    async def validate_user_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if is_valid_email(slot_value) == "UNDELIVERABLE":
            dispatcher.utter_message(
                text=f"Em kiểm tra thấy email '{slot_value}' không tồn tại hoặc không thể tương tác. Vui lòng nhập lại")
            return {"user_email": None}

        return {"user_email": slot_value}


class ValidateEmailPhoneForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_email_phone_form"

    async def validate_user_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if is_valid_email(slot_value) == "UNDELIVERABLE":
            dispatcher.utter_message(
                text=f"Em kiểm tra thấy email '{slot_value}' không tồn tại hoặc không thể tương tác. Vui lòng nhập lại")
            return {"user_email": None}

        return {"user_email": slot_value}

    async def validate_user_phone(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        valid = is_valid_phone_number(slot_value)
        if valid is False or valid is None:
            dispatcher.utter_message(
                text=f"Em kiểm tra thấy số điên thoại '{slot_value}' không hợp lệ. Vui lòng nhập lại")
            return {"user_phone": None}

        return {"user_phone": slot_value}
