from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder

import re
import time as t
import json

# TODO: remove para .env
ENDPOINT='a1vjlljcvzaa14-ats.iot.us-east-1.amazonaws.com'
CLIENT_ID='computer'
PATTH_CERTIFICATE='Code/Operationalization/certificates/computer.cert.pem'
PATH_PRIVATE_KEY='Code/Operationalization/certificates/computer.private.key'
PATH_TO_AMAZON_ROOT_CA_KEY='Code/Operationalization/certificates/root-CA.crt'
TOPIC='computer/temperature'

def connect_aws_iot_core():
    event_loop = io.EventLoopGroup(1)
    host_resolver = io.DefaultHostResolver(event_loop)
    client_bootstrap = io.ClientBootstrap(event_loop, host_resolver)
    mqtt_connection = mqtt_connection_builder.mtls_from_path(
        endpoint=ENDPOINT,
        cert_filepath=PATTH_CERTIFICATE,
        pri_key_filepath=PATH_PRIVATE_KEY,
        ca_path=PATH_TO_AMAZON_ROOT_CA_KEY,
        client_bootstrap=client_bootstrap,
        client_id=CLIENT_ID,
        clean_session=False,
        keep_alive_secs=6

    )
    connection_future = mqtt_connection.connect()
    connection_future.result()
    return mqtt_connection, connection_future



def read_last_entries(current_line=0):
    with open('./Data/Processed/SP.csv', 'r') as entries:
        entries.seek(current_line)
        for line in entries:
            yield line

if __name__ == '__main__':
    read_from_line = 0
    mqtt_connection, connect = connect_aws_iot_core()
    for index, line in enumerate(read_last_entries(current_line=read_from_line)):
        words = re.split(',|\n', line)
        message = {
            'Index': words[0],
            'Region': words[1],
            'Country': words[2],
            'City': words[3],
            'Month': words[4],
            'Day': words[5],
            'Year': words[6],
            'Celsius': words[7],
            'Date': words[8] 
        }
        print('Sending message: {0}'.format(message))
        mqtt_connection.publish(topic=TOPIC,
                                payload=json.dumps(message),
                                qos=mqtt.QoS.AT_LEAST_ONCE)
        t.sleep(.1)
        
    read_from_line = index
    disconnect_future = mqtt_connection.disconnect()
    disconnect_future.result()
    t.sleep(4)