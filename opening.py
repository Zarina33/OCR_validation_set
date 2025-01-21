import subprocess
import logging
from pathlib import Path

# Настройка логгирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def open_images_in_preview(txt_file_path: str, start_line: int, end_line: int):
    """
    Открывает изображения в Preview на Mac из txt файла в указанном диапазоне строк
    
    Args:
        txt_file_path (str): Путь к txt файлу с путями к изображениям
        start_line (int): Номер начальной строки (с 1)
        end_line (int): Номер конечной строки
    """
    try:
        with open(txt_file_path, 'r', encoding='utf-8') as f:
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
                
            logger.info(f"Открытие изображений из строк {start_line} - {end_line}")
            
            # Собираем все пути к изображениям в указанном диапазоне
            image_paths = []
            for line in lines[start_line-1:end_line]:
                image_path = line.strip().split()[0]
                if Path(image_path).exists():
                    image_paths.append(image_path)
                else:
                    logger.error(f"Файл не найден: {image_path}")
            
            if image_paths:
                # Открываем все изображения в Preview одной командой
                subprocess.run(['open', '-a', 'Preview'] + image_paths)
                logger.info(f"Открыто {len(image_paths)} изображений в Preview")
            else:
                logger.error("Не найдено ни одного изображения для открытия")
                
    except Exception as e:
        logger.error(f"Ошибка: {e}")

def main():
    txt_file_path = '/Users/zarinamacbook/Desktop/valid/last.txt'
    
    try:
        start_line = int(input("Введите номер начальной строки: "))
        end_line = int(input("Введите номер конечной строки: "))
        
        logger.info("Запуск открытия изображений...")
        open_images_in_preview(txt_file_path, start_line, end_line)
        
    except ValueError:
        logger.error("Пожалуйста, введите корректные числа для диапазона строк")

if __name__ == "__main__":
    main()