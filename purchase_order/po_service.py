from nameko.rpc import rpc

import dependencies


class PurchaseOrderService:

    name = 'po_service'

    database = dependencies.Database()

    @rpc
    def get_all_po(self):
        purchase_order = self.database.get_all_po()
        return purchase_order

    @rpc
    def create_po(self, id_employee, id_supplier, detail_purchase_order):
        purchase_order = self.database.create_po(id_employee, id_supplier, detail_purchase_order)
        return purchase_order

    @rpc
    def create_detail_po(self, detail_purchase_order):
        result = self.database.create_detail_po(detail_purchase_order)
        return result

    @rpc
    def change_status_po(self, id, status):
        change_status_po = self.database.change_status_po(id, status)
        return change_status_po

    @rpc
    def edit_po(self, id, id_employee, id_supplier, status):
        purchase_order = self.database.edit_po(id, id_employee, id_supplier, status)
        return purchase_order

    @rpc
    def delete_po(self, id):
        result = self.database.delete_po(id)
        return result
    


    # @rpc
    # def update_booking(self, id_booking, id_room_new, id_room_type_new):
    #     updated_booking = self.database.update_booking_room(
    #         id_booking, id_room_new, id_room_type_new)
    #     return updated_booking

    # @rpc
    # def get_all_booking(self):
    #     booking = self.database.get_all_booking()
    #     return booking

    # @rpc
    # def get_booking_by_id(self, id):
    #     booking = self.database.get_booking_by_id(id)
    #     return booking

    # @rpc
    # def add_service(self, name, cost, status, last_update, last_update_by):
    #     service = self.database.add_service(
    #         name, cost, status, last_update, last_update_by)
    #     return service

    # @rpc
    # def get_all_service(self):
    #     service = self.database.get_all_service()
    #     return service

    # @rpc
    # def get_service_by_id(self, id):
    #     service = self.database.get_service_by_id(id)
    #     return service

    # @rpc
    # def add_detail_booking(self, id_service, id_booking, qty, price):
    #     detail_booking = self.database.add_detail_booking(
    #         id_service, id_booking, qty, price)
    #     return detail_booking

    # @rpc
    # def get_all_detail_booking(self):
    #     detail_booking = self.database.get_all_detail_booking()
    #     return detail_booking

    # @rpc
    # def get_detail_booking_by_id(self, id):
    #     detail_booking = self.database.get_detail_booking_by_id(id)
    #     return detail_booking

    # @rpc
    # def get_all_service_by_booking_id(self, id):
    #     detail_service_booking = self.database.get_all_service_by_booking_id(
    #         id)
    #     return detail_service_booking
