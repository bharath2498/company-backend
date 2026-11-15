from celery import shared_task


@shared_task
def generate_product_report():
    print("Generating product report in background...")
    return "Report completed"
