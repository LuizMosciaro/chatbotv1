from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    resp = MessagingResponse()
    msg = resp.message()

    incoming_msg = request.values.get('Body', '').lower()

    #Extrato
    if incoming_msg == '1':
        msg.body('Escolha uma opção:\n1.1 Últimos 7 dias\n1.2. Últimos 15 dias\n1.3. Últimos 30 dias')
    elif incoming_msg == '1.1':
        msg.body('''
            Extrato dos últimos 7 dias:

            1. Depósito - R$ 500,00
            2. Saque - R$ 100,00
            3. Pagamento de conta - R$ 50,00
            4. Transferência recebida - R$ 200,00
            5. Compra - R$ 75,00
        ''')
    elif incoming_msg == '1.2':
        msg.body('''
            Extrato dos últimos 15 dias:

            1. Pagamento de conta - R$ 80,00
            2. Transferência enviada - R$ 150,00
            3. Saque - R$ 50,00
            4. Depósito - R$ 300,00
            5. Compra - R$ 25,00
        ''')
    elif incoming_msg == '1.3':
        msg.body('''
            Extrato dos últimos 30 dias:

            1. Transferência recebida - R$ 100,00
            2. Depósito - R$ 200,00
            3. Pagamento de conta - R$ 70,00
            4. Compra - R$ 45,00
            5. Saque - R$ 30,00
        ''')

    #Transferencias
    elif incoming_msg == '2':
        msg.body('Escolha uma opção:\n2.1. Transferência entre contas do mesmo banco\n2.2. Transferência para outro banco\n2.3. Transferência internacional')
    elif incoming_msg == '2.1' or incoming_msg == '2.2' or incoming_msg == '2.3':
        msg.body('Sistema indisponível no momento. Tente novamente mais tarde')

    #Cartões
    elif incoming_msg == '3':
        msg.body('Escolha uma opção:\n3.1 Fatura do cartão\n3.2 Perda do cartão\n3.3 Gerar boleto de pagamento')
    elif incoming_msg == '3.1':
        msg.body('''
            Fatura do Cartão de Crédito:

            Nome do Cliente: Luiz E** V** M**
            Número do Cartão: **** **** **** 3456
            Data de Vencimento: 10/07/2099

            Descrição das Transações:
            1. Compra - R$ 150,00
            2. Restaurante - R$ 80,00
            3. Supermercado - R$ 200,00
            4. Viagem - R$ 500,00
            5. Pagamento de Conta - R$ 100,00

            Total: R$ 1.030,00
        ''')
    elif incoming_msg == '3.2':
        msg.body('''
            Menu de Relato de Perda de Cartão Bancário:
            3.2.1 Cartão de Débito
            3.2.2 Cartão de Crédito
            3.2.3 Outros Cartões

            Digite o número correspondente à opção desejada:
        ''')
    elif incoming_msg == '3.2.1' or incoming_msg == '3.2.2' or incoming_msg == '3.2.3':
        msg.body('''
            Ligue para a Central de Atendimento de Cartões: 0800-5959-555. Se prefirir abra um chamado online: www.atedimentocartoesbrix.com.br
        ''')
    elif incoming_msg == '3.3':
        msg.body('O código do boleto bancário deste mês é: 34191.09008 64771.277459 64001.015008 5 88280000015000')

    else:
        msg.body('Escolha uma opção digitando o número correspondente:\n1. Extrato\n2. Transferências\n3. Cartões')

    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
