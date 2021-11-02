
from flask_restful import Resource,  reqparse
from flask_jwt import  jwt_required
from models.item import ItemModel

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
                            type=float,
                            required=True,
                            help="This should be provided!")   

    parser.add_argument('store_id',
                            type=int,
                            required=True,
                            help="This should be provided!")                           

    @jwt_required()
    def get(self , name):
        item= ItemModel.find_by_name(name)
        if item:
            return item.json()
        else:
            return {"message":"No record Found"} , 404
    
    @jwt_required()
    def post(self , name):
        result = ItemModel.find_by_name(name)
        if result:
            return {'message':'An item with name {} already exist.'.format(name)} , 400

        data = Item.parser.parse_args()
        item = ItemModel(name,data['price'],data['store_id'])
        try:
            item.save_to_db()
        except:
            return {"message":"An exception has occured"},500
        return item.json(), 201


    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name,data['price'],data['store_id'])
        else:
            item.price = data['price']
        item.save_to_db()
        return item.json()


    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        


    
class ItemList(Resource):
    def get(self):
        return {"items":[item.json() for item in ItemModel.query.all()]}