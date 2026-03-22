def io_handler(filename: str) -> tuple[int, list[int]]:
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    if not lines:
        return 0, []
        
    frames = int(lines[0].strip())
    # O primeiro número do arquivo é a quantidade de quadros, o restante as páginas
    pages = [int(line.strip()) for line in lines[1:] if line.strip()]
    
    return frames, pages