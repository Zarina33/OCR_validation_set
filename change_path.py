def update_paths_in_txt(input_txt, output_txt):
    """
    Replace file paths in TXT file.
    Args:
        input_txt (str): Path to the input TXT file
        output_txt (str): Path to save the updated TXT file
    """
    # Определяем старый и новый пути
    old_path = '/mnt/ks/Works/railcars/railcars_new/valid_codes/new_23_01_25/'
    new_path = '/Users/zarinamacbook/Desktop/valid/new_23_01_25/'

    try:
        # Читаем входной файл
        with open(input_txt, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()

        # Заменяем пути в каждой строке
        updated_lines = []
        for line in lines:
            # Заменяем только путь
            updated_line = line.replace(old_path, new_path)
            updated_lines.append(updated_line)

        # Записываем обновленные строки в выходной файл
        with open(output_txt, 'w', encoding='utf-8') as outfile:
            outfile.writelines(updated_lines)
            
        print(f"Обновлено и сохранено в {output_txt}")
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    input_txt = "/Users/zarinamacbook/Desktop/valid/new_23_01_25.txt"
    output_txt = "/Users/zarinamacbook/Desktop/valid/23_01_25.txt"
    update_paths_in_txt(input_txt, output_txt)
