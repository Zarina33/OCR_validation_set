from PIL import Image
import os

def crop_image(input_path, output_path, top=500, height=147):
    """
    Crops the bottom part of the image with specified parameters.
    
    Args:
        input_path (str): Path to the input image
        output_path (str): Path where to save the cropped image
        top (int): Distance from the top of the image to start cropping
        height (int): Height of the cropped section
    """
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Get original width
            width = img.width
            
            # Define the cropping box (left, top, right, bottom)
            crop_box = (0, top, width, top + height)
            
            # Crop the image
            cropped_img = img.crop(crop_box)
            
            # Save the cropped image
            cropped_img.save(output_path)
            print(f"Successfully cropped image saved to {output_path}")
            
    except Exception as e:
        print(f"Error processing image: {e}")

# Example usage
if __name__ == "__main__":
    # Путь к папке с изображениями
    input_folder = "/Users/zarinamacbook/Desktop/valid"
    # Путь к папке где сохранить результаты
    output_folder = "/Users/zarinamacbook/Desktop/valid/cropped"
    
    # Создаём папку для результатов если её нет
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Обрабатываем все файлы в папке
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):  # Проверяем расширение файла
            # Формируем полные пути к файлам
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"cropped_{filename}")
            
            # Обрабатываем изображение
            crop_image(input_path, output_path)