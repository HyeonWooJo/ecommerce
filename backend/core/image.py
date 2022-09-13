# 이미지 업로드 경로
def image_upload_path(instance, filename):
    return f"{instance.product.id}/{filename}"