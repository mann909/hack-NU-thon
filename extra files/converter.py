import json

def generate_chatbot_data(input_file_path, output_file_path):
    # Read the input JSON file
    with open(input_file_path, 'r') as input_file:
        data = json.load(input_file)

    # Create a list to store chatbot data
    chatbot_data = []

    # Loop through the products and generate chatbot data
    i=0
    for product in data:
        i+=1
        # print(product)
        chatbot_item = {
            "tag": f"product-{i}",
            "patterns": [],
            "responses": []
        }

        # Add product name and description to patterns
        chatbot_item["patterns"].append(product["ProductName"])
        chatbot_item["patterns"].append(product["Description"])

        # Add responses
        response = f"Brand: {product['ProductBrand']}, "
        response += f"Price: INR {product['Price (INR)']}, "
        response += f"Gender: {product['Gender']}, "
        response += f"Color: {product['PrimaryColor']}"
        # Add more attributes as needed
        chatbot_item["responses"].append(response)

        # Add the chatbot item to the list
        chatbot_data.append(chatbot_item)

    # Write the chatbot data to the output JSON file
    with open(output_file_path, 'w') as output_file:
        json.dump(chatbot_data, output_file, indent=2)

# Example usage:
input_file_path = 'myntra_products_catalog.json'  # Path to your input JSON file containing product data
output_file_path = 'mainFile.json'  # Path to the output JSON file you want to create for the chatbot
generate_chatbot_data(input_file_path, output_file_path)
