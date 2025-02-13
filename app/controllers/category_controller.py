from flask import Blueprint, jsonify
from app.models.models import Category

category_bp = Blueprint('category', __name__)

@category_bp.route('/categories/<int:id>', methods=['GET'])
def get_category_by_id(id):
    category = Category.query.get(id)
    if not category:
        return jsonify({"message": "Category not found"}), 404

    return jsonify({"message": "Category fetched successfully", "category": category.to_dict()}), 200



@category_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify(status='OK', service='user-read'), 200


