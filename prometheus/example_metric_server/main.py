from prometheus_client import start_http_server, Summary, Counter, REGISTRY, Gauge, Info
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

c = Counter('my_failures_example', 'Description of counter')
#REGISTRY.register(c)

s = Summary('plc_point_value', 'Description of summary')

from prometheus_client import Gauge
g = Gauge('my_inprogress_requests', 'Description of gauge')

i = Info('my_build_version', 'Description of info')




def process_random():
    c.inc(1)
    s.observe(4.7)
    g.set(random.random())
    i.info({'version': '1.2.3', 'buildhost': 'foo@bar'})
    print("+1.6")

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request(random.random())
        process_random()
