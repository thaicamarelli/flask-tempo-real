import uuid
import qrcode

class Pix:
    def __init__(self):
        pass

    def create_payment(self) -> dict:
        bank_payment_id = str(uuid.uuid4())

        # codigo copia e cola
        hash_payment = f'hash_payment_{bank_payment_id}'

        # qr_code
        img = qrcode.make(hash_payment)
        # salvar imagem como arquivo PNG
        img.save(f"static/img/qr_code_payment_{bank_payment_id}.png")

        return {"payment_bank_id": bank_payment_id,
                "qr_code": f"qr_code_payment_{bank_payment_id}"}