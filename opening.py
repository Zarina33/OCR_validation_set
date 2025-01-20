import cv2
import logging
from pathlib import Path

# Настройка логгирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def show_images_from_txt(txt_file_path: str, start_line: int, end_line: int):
    """
    Открывает изображения из txt файла в указанном диапазоне строк
    
    Args:
        txt_file_path (str): Путь к txt файлу с путями к изображениям
        start_line (int): Номер начальной строки (с 1)
        end_line (int): Номер конечной строки
    """
    try:
        with open(txt_file_path, 'r', encoding='utf-8') as f:
            # Читаем все строки
            lines = f.readlines()
            
            # Проверяем корректность диапазона
            total_lines = len(lines)
            if start_line < 1:
                start_line = 1
            if end_line > total_lines:
                end_line = total_lines
            if start_line > end_line:
                logger.error("Начальная строка больше конечной")
                return
                
            logger.info(f"Показ изображений из строк {start_line} - {end_line}")
            
            # Обрабатываем только строки в указанном диапазоне
            for line_num, line in enumerate(lines[start_line-1:end_line], start_line):
                # Получаем путь к изображению (первая часть строки до табуляции)
                image_path = line.strip().split('\t')[0]
                
                # Проверяем существование файла
                if not Path(image_path).exists():
                    logger.error(f"Файл не найден: {image_path}")
                    continue
                
                # Загружаем и показываем изображение
                image = cv2.imread(image_path)
                if image is None:
                    logger.error(f"Не удалось загрузить изображение: {image_path}")
                    continue
                
                # Показываем изображение
                window_name = f'Image {line_num}'
                cv2.imshow(window_name, image)
                
                # Ждем нажатия клавиши
                key = cv2.waitKey(0)
                
                # Закрываем текущее окно
                cv2.destroyWindow(window_name)
                
                # Если нажата клавиша 'q' или ESC, прерываем просмотр
                if key in [ord('q'), 27]:
                    break
                    
        logger.info("Просмотр завершен!")
        
    except FileNotFoundError:
        logger.error(f"Файл не найден: {txt_file_path}")
    except Exception as e:
        logger.error(f"Ошибка при обработке файла: {e}")

def main():
    # Путь к txt файлу с путями к изображениям
    txt_file_path = '/mnt/ks/Works/railcars/railcars_new/valid_codes/ocr_results.txt'
    
    # Запрашиваем диапазон строк
    try:
        start_line = int(input("Введите номер начальной строки: "))
        end_line = int(input("Введите номер конечной строки: "))
        
        logger.info("Запуск просмотра изображений...")
        show_images_from_txt(txt_file_path, start_line, end_line)
        
    except ValueError:
        logger.error("Пожалуйста, введите корректные числа для диапазона строк")

if __name__ == "__main__":
    main()
