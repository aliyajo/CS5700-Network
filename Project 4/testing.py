#!/usr/bin/env -S python3 -u

def check_for_corruption( msg):
        '''
        This function checks for corruption in the message.
        Params:
            @msg: The message to check for corruption
        '''
        # Calculate the checksum of the message
        checksum = 0
        for char in msg["data"]:
            checksum += ord(char)
        # Check if the checksum is correct
        if checksum != msg["checksum"]:
            print(f"Corrupted data; {msg['sequence']}")
            return checksum
    
def main():
    msg = {"sequence": 0, "checksum": 0, "data": "----- Block 0000011 -----4e1ea06ac35946390398c55ee76594182005ef003924cf7aa226dd40f403922ceae48143fb3926de3ac0070ec4e72367a0e1768415ee65f30c00cdb00d0b94d71c53ef3069f9f00506c109de20709d895861f9d75f519d920fc0d0ca96b21156c8f1829360444e57dc648d87dc83a817656ed1d739300abd72f28e97a85d7917234111e8c346a7cad5280fc0f4d37aa02bc70bc2ca866d4c23552a8c91ef1f889e531930f0f67111eb544383b98603551f51280dfd0b180cf58240f9c8abcd4831aa024987d1601c8acc8b23b9910a28a05eb3f6ed2782af5354f26dc41f9515f489c894b1470f9c2e4d6a2f9f0f9f679278ef0a338eea0dc8f977bb2ee7e502fb17cddb4571993c80f712d568ce30c2aa5f782907084df25e6705c0db072d6f8d8611f24e115e3d52947241679056e5c130c5b347dcf51400a50b3f80ec9f5b9e21d65dff856d776aec12120dc9350da2e703dd926823194add2f0cb498c4f4135eab3c47df90accdb6358cc328f12f5354a8b49cdeedd3bbb3f5ca4bf9ebd6be83e3f567748acd12b1cfb458183abd332ae0e9fd74e9381fd38bfcda2011dbc907fb987d2caa3da336841c764af2de49c2fb99ad779ef6de802a28c40df461a6c24a75202f875de31f2ed7262431a62ef4be4ff09bcddb7f3fee594faf5a1f816a57cc91dc0a3c857f8826839616c8cf5b05f6f389e044def0054750f03f7988846ba536f8ce3b86eb9e8b7ea06e7895e677a6ffcd45dad37471546950f072bf558c6ef141e4079b9d55a968b8574628703a9c4845138942b168f63b667f35a346e922ca0d760f131674b053dae0864b430da05e58ae2b07904baab145a26d75e7bb9a4794ca26d6dde8ec6b33424578b28fc02580798f1de4e436d0e11373e72a358b6c90c17203a1ca60e9c6fdbc794f46b734f28f4923fa69e151c21f10d54067"}

    print(check_for_corruption(msg))

if __name__ == "__main__":
    main()