
# Conceito SOLID => Cada classe deve ter uma única responsabilidade.

class EmailSender:
    def send_email(self, recipient, subject, body):
        # Lógica para envio de email
        print(f"Email sent to {recipient}")

class OrderProcessor:
    def __init__(self, email_sender):
        self.email_sender = email_sender

    
    def process_order(self, order):
        # Processamento do pedido
        print(f"Processing order: {order}")
        self.email_sender.send_email(order.customer_email, "order confirmation", "Your order has been processed.")

class Order:
    def __init__(self, customer_email):
        self.customer_email = customer_email


if __name__ == "__main__":
    email_sender = EmailSender()
    order_processor = OrderProcessor(email_sender)

    order = Order("rosbiff@elhombre.com")
    order_processor.process_order(order)

    
