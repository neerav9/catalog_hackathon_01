functional_items = []
non_functional_items = []
recyclable_items = []

def determine_condition(device_type, years_of_service):
    average_life = {
        'Laptop': 5,
        'Smartphone': 3,
        'Printer': 7,
        'Tablet': 4,
        'Desktop': 6,
        'Projector': 6
    }
    
    if device_type in average_life:
        remaining_life = max(average_life[device_type] - years_of_service, 0)
    else:
        remaining_life = "Unknown"
    
    return remaining_life

def add_item(name, device_type, quantity, years_of_service, condition):

    remaining_life = determine_condition(device_type, years_of_service)
    
    if remaining_life == 0 or condition.lower() == "poor":
        status = "Non-functional"
        non_functional_items.append({
            'name': name,
            'device_type': device_type,
            'quantity': quantity,
            'years_of_service': years_of_service,
            'remaining_life': remaining_life,
            'condition': condition,
            'status': status
        })
    elif condition.lower() == "good" and remaining_life <= 2:
        status = "Recyclable"
        recyclable_items.append({
            'name': name,
            'device_type': device_type,
            'quantity': quantity,
            'years_of_service': years_of_service,
            'remaining_life': remaining_life,
            'condition': condition,
            'status': status
        })
    else:
        status = "Functional"
        functional_items.append({
            'name': name,
            'device_type': device_type,
            'quantity': quantity,
            'years_of_service': years_of_service,
            'remaining_life': remaining_life,
            'condition': condition,
            'status': status
        })
    
    print(f"Added {quantity} of {name} ({device_type}) with status '{status}'.")

def update_item_status(name, new_status):
    all_items = functional_items + non_functional_items + recyclable_items
    for item in all_items:
        if item['name'] == name:
            if item in functional_items:
                functional_items.remove(item)
            elif item in non_functional_items:
                non_functional_items.remove(item)
            elif item in recyclable_items:
                recyclable_items.remove(item)
            
            item['status'] = new_status
            
            if new_status == "Non-functional":
                non_functional_items.append(item)
            elif new_status == "Recyclable":
                recyclable_items.append(item)
            else:
                functional_items.append(item)
                
            print(f"Updated {name} status to '{new_status}'.")
            return
    print(f"Item {name} not found.")

def replace_non_functional_items():
    """Replace non-functional items with functional items of the same type and maintain a count."""
    global non_functional_replacements
    non_functional_replacements = 0
    for item in non_functional_items[:]: 
        replacement_found = False
        for functional_item in functional_items:
            if functional_item['device_type'] == item['device_type']:
                print(f"\nReplacing {item['name']} ({item['device_type']}) - {item['quantity']} units")
                
                add_item(f"Replacement {item['name']}", item['device_type'], item['quantity'], 0, "Good")
                
                non_functional_items.remove(item)
                non_functional_replacements += 1
                replacement_found = True
                break
        if not replacement_found:
            print(f"No functional item found to replace {item['name']}.")
    
    print(f"\nTotal non-functional items replaced: {non_functional_replacements}")

def recycle_recyclable_items():
    """Recycle all recyclable items and maintain a count."""
    global recyclable_recycled
    recyclable_recycled = 0
    for item in recyclable_items[:]:  
        print(f"\nRecycling {item['name']} ({item['device_type']}) - {item['quantity']} units")
        
        recyclable_items.remove(item)
        recyclable_recycled += 1
    
    print(f"\nTotal recyclable items recycled: {recyclable_recycled}")

def get_report():
    """Generate a categorized report of all e-waste items."""
    print("\n" + "="*150)
    print("E-Waste Report".center(150))
    print("="*150)
    
    print("\nFunctional Items:")
    print("-" * 150)
    print(f"{'Name':<30} {'Device Type':<20} {'Quantity':<10} {'Years of Service':<20} {'Remaining Life':<20} {'Condition':<15} {'Status':<15}")
    print("-" * 150)
    for item in functional_items:
        print(f"{item['name']:<30} {item['device_type']:<20} {item['quantity']:<10} {item['years_of_service']:<20} {item['remaining_life']:<20} {item['condition']:<15} {item['status']:<15}")
    print("-" * 150)
    
    print("\nNon-functional Items:")
    print("-" * 150)
    print(f"{'Name':<30} {'Device Type':<20} {'Quantity':<10} {'Years of Service':<20} {'Remaining Life':<20} {'Condition':<15} {'Status':<15}")
    print("-" * 150)
    for item in non_functional_items:
        print(f"{item['name']:<30} {item['device_type']:<20} {item['quantity']:<10} {item['years_of_service']:<20} {item['remaining_life']:<20} {item['condition']:<15} {item['status']:<15}")
    print("-" * 150)

def run_test_cases():
   
    add_item("Old Laptop 1", "Laptop", 1, 6, "Poor")
    add_item("Old Laptop 2", "Laptop", 2, 6, "Poor")
    add_item("Old Smartphone 1", "Smartphone", 1, 3, "Poor")
    add_item("Old Smartphone 2", "Smartphone", 2, 3, "Poor")
    add_item("Functional Laptop 1", "Laptop", 1, 1, "Good")
    add_item("Functional Laptop 2", "Laptop", 1, 1, "Good")
    add_item("Functional Smartphone 1", "Smartphone", 1, 1, "Good")
    add_item("Functional Smartphone 2", "Smartphone", 1, 1, "Good")
    
    get_report()
    replace_non_functional_items()
    recycle_recyclable_items()  
    
run_test_cases()
