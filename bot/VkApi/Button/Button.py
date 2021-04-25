class Button:

    GREEN = "positive"
    WHITE = "secondary"
    BLUE = "primary"
    RED = "negative"

    TYPE_CALLBACK = "callback"
    TYPE_TEXT = "text"

    json = {}
    payload = None
    label = None

    def __init__(self, payload):
        self.payload = payload
        action = {
            "type": self.TYPE_TEXT,
            "payload": "{\"button\": \"" + payload + "\"}",
            "label": self.label
        }
        self.json["action"] = action
        self.json["color"] = self.WHITE

    def set_color(self, color):
        self.json['color'] = color
        return self

    def set_link(self, url):
        self.json['action']['type'] = 'open_link'
        self.json['action']['link'] = url
        return self

    def set_payload(self, text):
        self.payload = text
        self.json['action']['payload'] = "{\"button\": \"" + text + "\"}"
        return self

    def set_text(self, text):
        self.json['action']['label'] = text
        return self

    def get(self):
        return self.json

    """
    public Button setLink(String url){
        this.json.get("action").getAsJsonObject().addProperty("type", "open_link");
        this.json.get("action").getAsJsonObject().addProperty("link", url);
        this.json.remove("color");
        return this;
    }

    public Button setType(String type){
        this.json.get("action").getAsJsonObject().addProperty("type", type);
        return this;
    }

    public Button setPayload(String text){
        this.payload = text;
        this.json.get("action").getAsJsonObject().addProperty("payload", "{\"button\": \"" + text + "\"}");
        return this;
    }

    public Button setText(String text){
        this.json.get("action").getAsJsonObject().addProperty("label", text);
        return this;
    }
"""