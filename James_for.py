#
# Erlinda韋琳達, 2025/09/24
# File: 0_template.py
# Short description of the task
#

# 1. Input
order_values = [120, 450, 80, 300, 650]
total_revenue = 0

# 2. Process
for order in order_values:
    total_revenue += order
    print (f"Processing order: ${order}")

# 3. Output
print (f"Total Revenue: ${total_revenue}")
