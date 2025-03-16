import os

# Define the documentation structure with filenames and headings
docs_structure = {
    "index.md": "# Welcome to IVEA Documentation\n\nThis is the official documentation for IVEA software.",
    "ivea-plugin-location.md": "# IVEA Plugin Location",
    "random-burst-event.md": "# Random Burst Event Overview",
    "random-burst-advanced-settings.md": "# Random Burst Event - Advanced Settings",
    "random-burst-output-results.md": "# Random Burst Event - Output Results",
    "stationary-event-tab.md": "# Stationary Event Tab Overview",
    "stationary-advanced-settings.md": "# Stationary Event Tab - Advanced Settings",
    "stationary-output-results.md": "# Stationary Event Tab - Output Results",
    "hotspot-area-extraction.md": "# Hotspot Area Extraction Overview",
    "hotspot-advanced-settings.md": "# Hotspot Area Extraction - Advanced Settings",
    "roi-multi-measurement.md": "# ROI Multi-Measurement Plugin",
    "labeling-new-data.md": "# Labeling New Data with the IVEA Data Labeling Plugin",
    "labeling-rois.md": "# Labeling ROIs in IVEA",
    "training-main-script.md": "# Training Using IVEA Python - Main Script GUI",
    "training-configuration-file.md": "# Training Using IVEA Python - Configuration File",
    "training-environment-setup.md": "# Training Using IVEA Python - Environment Setup",
    "training-running-debugging.md": "# Training Using IVEA Python - Running and Debugging",
    "faq.md": "# Frequently Asked Questions (FAQ)",
    "api.md": "# API Reference",
}

# Create each file and write its respective heading
for filename, content in docs_structure.items():
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content + "\n\n")
    print(f"Created {filename}")

print("\n✅ All documentation files have been generated successfully!")
