from .repositories.CrashReportDispatcher import CrashReportDispatcher

class ExtractorService(object):
    """ Deals with all actions related to extraction.

        This incudes:
            - purchase
            - crash reports
            - installs
    """

    def __init__(self):
        super(ExtractorService, self).__init__()

    def crash_report(self, user_id, timestamp, message):
        print("user_id: {}, timestamp: {}, message: {}".format(
            user_id, timestamp, message))

        dispatcher = CrashReportDispatcher()
        dispatcher.save(
            {
                'message': message,
                'timestamp': timestamp,
                'user_id': user_id               
            }
        )

        return {'status': 'success'}

    def purchase(self, user_id, timestamp, sku):
        print("user_id: {}, timestamp: {}, sku: {}".format(
            user_id, timestamp, sku))
        return {'status': 'success'}

    def install(self, user_id, timestamp):
        print("user_id: {}, timestamp: {}".format(
            user_id, timestamp))
        return {'status': 'success'}
