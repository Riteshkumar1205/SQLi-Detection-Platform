from burp import IBurpExtender, IHttpListener
import json

class BurpExtender(IBurpExtender, IHttpListener):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("SQLi Logger")
        callbacks.registerHttpListener(self)

    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        if messageIsRequest:
            request = self._helpers.analyzeRequest(messageInfo)
            headers = request.getHeaders()
            body = messageInfo.getRequest()[request.getBodyOffset():].tostring()
            with open("burp_logs.json", "a") as log:
                json.dump({"headers": list(headers), "body": body.decode(errors='ignore')}, log)
