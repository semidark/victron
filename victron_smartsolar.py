from os import name
from victron_gatt import AnyDevice, gatt_device_instance

# F9:8E:1C:EC:9C:72 SmartSolar HQ2027LDKCU
def init_sequence_template():
    stuff = [
        # very early, well-known endpoints.not needed for values
        #  ("0022":"0200"),
        #  ("0025":"0100"),
        ("0021", "fa80ff"),
        ("0021", "f980"),
        ("0024", "01"),
        ("0024", "0300"),
        ("0024", "060082189342102703010303"),
        ("0027", "05008119ec0f05008119ec0e05008119010c0500"),
        ("0024", "81189005008119ec3f05008119ec12"),
        ("0027", "0501811901000501811901000503811901000503"),
        ("0027", "8119010005038119edd405038119ec3f05038119"),
        ("0027", "ec12050381181805038119010205038119edbc05"),
        ("0027", "038119eddc05038119eddd05038119010a050381"),
        ("0027", "19014005038119015005038119020105038119ed"),
        ("0027", "da05038119edbb05038119eccb05038119eccd05"),
        ("0027", "038119eccc05038119ecdb05038119ecdd050381"),
        ("0024", "19ecdc05038119eceb05038119eced"),
        ("0027", "05038119ecec05038119ecfb05038119ecfd0503"),
        ("0027", "8119ecfc05038119edbd05038119edb805038119"),
        ("0027", "ed8d05038119ed8f05038119edec050381192211"),
        ("0027", "05038119221205038119eda805038119edad0503"),
        ("0027", "8119eda905038119034e05038119202705038119"),
        ("0027", "2004050381190207050381190205050381190244"),
        ("0027", "05038119020005038119020205038119ede80503"),
        ("0024", "810405038119edef05038119edf105038119edf0"),
        # 5sec
        ("0027", "05038119edf705038119edf605038119edf40503"),
        ("0027", "8119edfb05038119edfd05038119edf205038119"),
        ("0027", "ede605038119ede005038119ede205038119ed2e"),
        ("0027", "05038119ede305038119ede405038119ede50503"),
        ("0027", "8119edfe05038119ede705038119edca05038119"),
        ("0027", "d0c005038119ed2f05038119edab05038119ed9c"),
        ("0027", "05038119ed9d05038119ed9005038119ed9e0503"),
        ("0024", "8119ed9805038119edd905038119100a"),
        ("0021", "f941"),
        ("0027", "0503811903500503811903510503811903520503"),
        ("0027", "8119035305038119edba05038119edb905038119"),
        ("0027", "eda005038119eda105038119eda205038119eda3"),
        ("0027", "05038119eda405038119eda505038119ed9a0503"),
        ("0027", "8119ed9605038119ed9905038119ed9705038119"),
        ("0027", "ed9b05038119eda7050381192031050381190400"),
        ("0027", "05038119040405038119edce05038119eddf0503"),
        ("0024", "8119103005038119104f050381191050"),
        ("0021", "f941"),
        ("0027", "0503811910a00503811910510503811910a10503"),
        ("0027", "811910520503811910a205038119105305038119"),
        ("0027", "10a30503811910540503811910a4050381191055"),
        ("0027", "0503811910a50503811910560503811910a60503"),
        ("0027", "811910570503811910a705038119105805038119"),
        ("0027", "10a80503811910590503811910a905038119105a"),
        ("0027", "0503811910aa05038119105b0503811910ab0503"),
        ("0024", "8119105c0503811910ac05038119105d"),
        # 0.5sec
        ("0027", "0503811910ad05038119105e0503811910ae0503"),
        ("0027", "8119105f0503811910af05038119106005038119"),
        ("0027", "10b00503811910610503811910b1050381191062"),
        ("0027", "0503811910b20503811910630503811910b30503"),
        ("0027", "811910640503811910b405038119106505038119"),
        ("0027", "10b50503811910660503811910b6050381191067"),
        ("0027", "0503811910b70503811910680503811910b80503"),
        ("0024", "811910690503811910b905038119106a"),
        ("0021", "f941"),
        # 0.8sec
        ("0027", "0503811910ba05038119106b0503811910bb0503"),
        ("0027", "8119106c0503811910bc05038119106d05038119"),
        ("0027", "10bd05038119106e0503811910be050381189005"),
        ("0027", "0381189105008119ec1305008119ec1405008119"),
        ("0027", "ec1505008119ec1605008119ec30050181190102"),
        ("0027", "0501811901420503811901020503811901020501"),
        ("0027", "81189005018119ec3f05018119ec120501811901"),
        ("0024", "0205018119ec0f05018119ec0e05018119010c"),
        # 0.9sec
        ("0027", "0501811901100600821893421027060382192031"),
        ("0024", "422f020600821893421027"),
        ("0021", "f941"),
        # 3sec
        ("0021", "f941"),
        ("0024", "0600821893421027"),
        # 4sec
        ("0024", "0600821893421027"),
        # 1.7sec
        ("0021", "f941"),
        # 2sec
        ("0024", "0600821893421027"),
        # 4sec (22.7-19.3)
        ("0024", "0600821893421027"),
        ("0021", "f941"),
        # repetition after this
        # 3.375sec between 0600821893421027
        # +0sec between 0600821893421027 & f941
        # 0.5-2sec between  f941 & 0600821893421027
        ########### END copied from wireshark
    ]
    for packet in stuff:
        handle = packet[0]
        uuid = handle_uuid_map[handle]
        hs = packet[1]
        data = bytearray.fromhex(hs)
        yield (uuid, handle, data)


ping = [
    ("0024", "0300"),
    ("0021", "f941"),  # taken from phoenix, sends power & current
]

handle_uuid_map = {
    # handle "9abd"
    # service "": "00001801-0000-1000-8000-00805f9b34fb",
    # handle "68ab"
    # "000c": "00002a05-0000-1000-8000-00805f9b34fb",
    # handle "c1a0"
    # desc"000d": "00002902-0000-1000-8000-00805f9b34fb",
    # handle "9abd"
    # prim"": "68c10001-b17f-4d3a-a290-34ad6499937c",
    # handle "68ab"
    "0010": "68c10002-b17f-4d3a-a290-34ad6499937c",
    # handle "e4a0"
    # desc"": "00002902-0000-1000-8000-00805f9b34fb",
    # handle "68ab"
    "0013": "68c10003-b17f-4d3a-a290-34ad6499937c",
    # handle "9abd"
    # prim"": "97580001-ddf1-48be-b73e-182664615d8e",
    # handle "68ab"
    "0016": "97580002-ddf1-48be-b73e-182664615d8e",
    # handle "68ab"
    "0018": "97580003-ddf1-48be-b73e-182664615d8e",
    # handle "2560"
    # decsr"": "00002902-0000-1000-8000-00805f9b34fb",
    # handle "68ab"
    "001b": "97580004-ddf1-48be-b73e-182664615d8e",
    # handle "68ab"
    "001d": "97580006-ddf1-48be-b73e-182664615d8e",
    # handle "ece0"
    # descr"": "00002902-0000-1000-8000-00805f9b34fb",
    # handle "9abd"
    # primary"": "306b0001-b081-4037-83dc-e59fcc3cdfd0",
    # handle "68ab"
    "0021": "306b0002-b081-4037-83dc-e59fcc3cdfd0",
    # handle "ec00"
    # desc"": "00002902-0000-1000-8000-00805f9b34fb",
    # handle "68ab"
    "0024": "306b0003-b081-4037-83dc-e59fcc3cdfd0",
    # handle "ed80"
    # descr"": "00002902-0000-1000-8000-00805f9b34fb",
    # handle "68ab"
    "0027": "306b0004-b081-4037-83dc-e59fcc3cdfd0",
    # handle "ed00"
    # descr"": "00002902-0000-1000-8000-00805f9b34fb",
}


def get_device_instance(mac, name, handle_single_value, handle_bulk_values):
    UUID_FUNCTION_TABLE = {
        handle_uuid_map["0027"]: handle_bulk_values,
        handle_uuid_map["0024"]: handle_single_value,
        # handle_uuid_map["0021"]: handle_single_value, # only f901 - answer to f941?!
    }

    return gatt_device_instance(
        mac,
        notification_table=UUID_FUNCTION_TABLE,
        ping=ping,
        handle_uuid_map=handle_uuid_map,
        name=name,
        init_sequence_template=init_sequence_template,
    )