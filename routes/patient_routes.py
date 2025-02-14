from flask import Blueprint, request, jsonify
from services.patient_service import extract_batch_data, extract_batch_data2  # Correct Import

patient_bp = Blueprint('patient_routes', __name__)

@patient_bp.route('/get-batch-data', methods=['GET'])
def get_batch_data():
    """
    API endpoint to fetch all patient data from a batch folder.
    """
    batch_name = request.args.get('batch_name')

    if not batch_name:
        return jsonify({"error": "Missing batch_name"}), 400

    data = extract_batch_data(batch_name)
    return jsonify(data)

@patient_bp.route('/get-batch-data2', methods=['GET'])
def get_batch_data2():
    """
    API endpoint to fetch all patient data from a batch folder.
    """
    batch_name = request.args.get('batch_name')

    if not batch_name:
        return jsonify({"error": "Missing batch_name"}), 400

    data = extract_batch_data2(batch_name)
    return jsonify(data), 200