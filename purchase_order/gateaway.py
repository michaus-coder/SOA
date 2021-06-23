import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http


class GatewayService:
    name = 'gateway'

    po_rpc = RpcProxy('po_service')

    @http('GET', '/purchase_order/')
    def get_po(self, request):
        po = self.po_rpc.get_all_po()
        return json.dumps(po)

    @http('POST', '/purchase_order/')
    def create_po(self, request):
        payload = json.loads(request.get_data(as_text=True))
        new_po = self.po_rpc.create_po(payload['id_employee'], payload['id_supplier'], payload['detail_purchase_order'])
        return json.dumps(new_po)

    @http('PUT', '/status_purchase_order/')
    def change_status_po(self, request):
        payload = json.loads(request.get_da(as_text=True))
        change_status = self.po_rpc.change_status_po(payload['id'], payload['status'])
        return json.dumps(change_status)

    @http('PUT', '/purchase_order/')
    def edit_po(self, request):
        payload = json.loads(request.get_da(as_text=True))
        edit = self.po_rpc.edit_po(payload['id'], payload['id_employee'], payload['id_supplier'], payload['status'])
        return json.dumps(edit)

    @http('DELETE', '/purchase_order/<string:id>')
    def delete_po(self, id):
        id = self.po_rpc.delete_po(id)
        return "PO with id: " + id + " has been successfully deleted."

    # @http('GET', '/room/<string:room_id>')
    # def get_room_by_id(self, request, room_id):
    #     room = self.po_rpc.get_room_by_id(room_id)
    #     return json.dumps(room)

    # @http('POST', '/purchase_order/')
    # def add_customer(self, request):
    #     payload = json.loads(request.get_data(as_text=True))
    #     customer_id = self.po_rpc.add_customer(payload['name'], payload['citizen_number'], payload['date_of_birth'], payload['gender'], payload['address'],
    #                                               payload['email'], payload['phone_number1'], payload['phone_number2'], payload['status'], payload['last_update'], payload['last_update_by'])
    #     return json.dumps(customer_id)

    # @http('DELETE', '/room/<string:room_number>')
    # def delete_room(self, request, room_number):
    #     room_number = self.po_rpc.delete_room(room_number)
    #     return "Room with number: " + room_number + " has been successfully deleted."

    # @http('PUT', '/room/<string:room_number>')
    # def change_room_status(self, request, room_number):
    #     room = self.po_rpc.change_room_status(room_number)
    #     return json.dumps(room)
