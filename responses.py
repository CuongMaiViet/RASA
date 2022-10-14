from channels import Channels
from functions import read_json

CHANNEL_SUPPORT_CW = ["ChannelWebWidget", "ChannelApi"]
CW_MSG_TYPE = ["input_select", "form", "cards", "article"]

CHANNEL_SUPPORT_RASA = ["ChannelTelegram"]
RASA_MSG_TYPE = ["rasa_button"]

class Responses:
    def __init__(self, channel, user_title, user_name) -> None:
        self.channel = channel
        self.title = user_title
        self.user_name = user_name

        self.emojis = read_json("emojis.json")

    def generate_response_skeleton(self):
        channel = self.channel
        if channel in CHANNEL_SUPPORT_CW:
            return {"content": "", "content_type": "", "content_attributes": {"items": []}, "private": False}
        elif channel in CHANNEL_SUPPORT_RASA:
            return {"text": "", "buttons": []}
        return None

    def get_channel_data(self):
        channel = self.channel
        json = Channels(self.title, self.user_name)
        if channel is None:
            return "missing channel"
        if channel in CHANNEL_SUPPORT_CW:
            return json.ChannelSupportCW()
        elif channel in CHANNEL_SUPPORT_RASA:
            return json.ChannelSupportRasa()
        # data = eval(
        #     f"__import__('{DATA_FILE_NAME}').Channels('{self.title}').{self.channel}()")
        return None

    def get_response_by_intent(self, intent):
        skeleton = self.generate_response_skeleton()
        if skeleton is None:
            return "missing skeleton"

        raw = self.get_channel_data()
        if raw is None:
            return "missing data"

        data = raw.get(intent)
        if not data:
            return "cannot get data from intent"

        message = data.get("message")
        message_type = data.get("message_type")
        payload = data.get("payload")

        if not message_type:
            return "missing message_type"

        channel = self.channel
        if channel in CHANNEL_SUPPORT_CW and message_type in CW_MSG_TYPE:
            skeleton["content"] = message
            skeleton["content_type"] = message_type
            skeleton["content_attributes"]["items"] = payload
            return skeleton
        elif channel in CHANNEL_SUPPORT_RASA and message_type in RASA_MSG_TYPE:
            skeleton["text"] = message
            skeleton["buttons"] = payload
            return skeleton

        if message_type == "no_payload":
            return message

        elif message_type == "full_of_text":
            text_menu = ""
            for val in payload:
                title = val.get("title")
                text_menu += f"{self.emojis.get('check_mark_button')} {title}\n"
            if isinstance(message, str):
                new_msg = []
                new_msg.append(message)
                new_msg.append(text_menu.strip())
                return new_msg
            
            message.append(text_menu.strip())
            return message

        return "Tham số message_type không phù hợp với kênh hiện tại"

    def get_bot_responses(self, dispatcher, intent):
        bot_response = self.get_response_by_intent(intent)
        # print(bot_response)
        if bot_response is None:
            dispatcher.utter_message(text=f"Lỗi không có phản hồi từ bot")

        if isinstance(bot_response, list):
            for val in bot_response:
                dispatcher.utter_message(text=val)
        elif isinstance(bot_response, dict):
            msg = bot_response.get("content")
            type = bot_response.get("content_type")

            if isinstance(msg, list):
                for val in msg[:-1]:
                    dispatcher.utter_message(text=val)
                if type == "cards":
                    bot_response["content_attributes"]["items"][0]["description"] = msg.pop()     
                bot_response["content"] = msg.pop()

            dispatcher.utter_message(json_message=bot_response)
            if type == "cards":
                dispatcher.utter_message(text=f"Mai rất sẵn lòng trả lời nếu {self.title} muốn biết thêm điều gì khác ^^")
        else:
            dispatcher.utter_message(text=f"Lỗi định dạng ({type(bot_response)})")
    