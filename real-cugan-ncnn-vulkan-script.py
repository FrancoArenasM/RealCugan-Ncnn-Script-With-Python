# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 17:39:42 2023

@author: Franco Arenas Mamani
E-mail: francoarenas1234567@gmail.com

"""
def main_global():   
        def main_image():
            import subprocess
            import os
            import tkinter as tk
            from tkinter import filedialog
            def select_image_file():
                print("Selecione la imagen que desea reescalar")
                root = tk.Tk()
                root.withdraw()
                image_file_path = filedialog.askopenfilename(title = "Seleccione una imagen PNG o JPG")
                _, ext = os.path.splitext(image_file_path)
                while ext not in ['.jpg', '.JPG', '.png', '.PNG']:
                    print("Formato de archivo no válido. Por favor, seleccione un archivo JPG o PNG.")
                    image_file_path = filedialog.askopenfilename(title = "Archivo")
                    _, ext = os.path.splitext(image_file_path)
                return image_file_path    
            def select_image_folder():
                print("La naturaleza del proceso implica la creacion de archivos")
                print("Selecciona el lugar donde se va a trabajar para el rescaldo")
                root = tk.Tk()
                root.withdraw()
                image_folder = filedialog.askdirectory(title = "Lugar donde se va a trabjar")
                root.destroy()
                image_folder = os.path.join(image_folder, 'Imagen_Rescaled')
                if not os.path.exists(image_folder):
                    os.makedirs(image_folder)
                return image_folder 
            def preguntar_image_scale():
                image_scale = input("Elige una relación de escala (2/3/4): ")
                while image_scale not in ["2", "3", "4"]:
                    print("Entrada no válida. Por favor, elige una relación de escala válida entre 2,3,4")
                    image_scale = input("Elige una relación de escala (2/3/4): ")
                return image_scale
            def preguntar_image_noise():
                valid_options = ["-1","0","1","2","3"] if image_scale == "2" else ["-1", "0", "3"]
                image_noise = input(f"Elige tratameinto del nivel de ruido {valid_options}: ")
                while  image_noise not in valid_options:
                    print(f"Entrada no válida. Por favor, elige un tratamiento de nivel de ruido válido entre {valid_options}")
                    image_noise = input("Elige tratamiento del nivel de ruido: ")
                return  image_noise
            def preguntar_usar_parametro_x():
                print("¿Desea utilizar la opción de aumento de tiempo de prueba (TTA)? Tenga en cuenta que no todas las tarjetas de video son compatibles con él, y también puede aumentar el tiempo de procesamiento.")
                usar_parametro_x = input(" (s/n): ")
                while usar_parametro_x not in ["s", "n"]:
                    print("Entrada no válida. Por favor, elige s o n")
                    usar_parametro_x = input(" (s/n): ")
                return usar_parametro_x
    
            def real_cugan_ncnn(image_file_path, image_folder, image_scale, image_noise):
                img_scaled_path =  image_folder + "/imagen_escalada.png"
                real_cugan_exe = os.path.join("C:\\", "realcugan-ncnn-vulkan", "realcugan-ncnn-vulkan.exe")
                usar_parametro_x = preguntar_usar_parametro_x()
                if usar_parametro_x == "s":
                    subprocess.run([real_cugan_exe, "-i", image_file_path, "-o", img_scaled_path, "-n", image_noise, "-s", image_scale, "-f", "png", "-c", "3", "-x", "-v"])
                else:
                    subprocess.run([real_cugan_exe, "-i", image_file_path, "-o", img_scaled_path, "-n", image_noise, "-s", image_scale, "-f", "png", "-c", "3", "-v"])
            print("Bienvenido al script de Franco para usar Real-CUGAN ncnn Vulkan  con una imagen")

            image_file_path = select_image_file()
            image_folder = select_image_folder()
            image_scale = preguntar_image_scale()
            image_noise = preguntar_image_noise()
            real_cugan_ncnn(image_file_path, image_folder, image_scale, image_noise)
            while True:
                choice_image = input("¿Desea reescalar otra imagen? (y/N) ")
                if choice_image == "y" or choice_image == "Y":
                    main_image()
                elif choice_image == "N" or choice_image == "n":
                    break
        
        def main_video():
            import subprocess
            import shutil
            import random
            import os
            import tkinter as tk
            from tkinter import filedialog
            from tkinter import Tk
            def select_video_file():
                print("Selecciona el video que desea reescalar")
                root = tk.Tk()
                root.withdraw()
                video_file_path = filedialog.askopenfilename(title = "Videos", filetypes=[("Videos mp4 y mkv", "*.mp4;*.mkv")])
                ext = os.path.splitext(video_file_path)[-1].lower()
                if ext == ".mp4" or ext == ".mkv":
                    return video_file_path
                else:
                    print("El archivo seleccionado no es un video en formato mp4 o mkv")
                    
                while  video_file_path is None:
                    video_file_path = select_video_file()
                return video_file_path
            def select_video_folder():
                print("La naturaleza del proceso implica la creacion de archivos y carpetas temporales")
                print("Selecciona el lugar donde se va a trabajar")
                root = Tk()
                root.withdraw()
                video_frames_folder = filedialog.askdirectory(title = "Carpeta donde se va a trabajar")
                root.destroy()
                return video_frames_folder
            
            def select_video_frames():
                frames_slect = os.path.join(video_frames_folder,'frames_select')
                if not os.path.exists(frames_slect):
                    os.makedirs(frames_slect)
                return frames_slect
            
            def extract_video_frames(video_file_path):
                frames_file = os.path.join(video_frames_folder, 'video_frames')
                ff_path = os.path.join(frames_file, "%09d.jpg")
                if not os.path.exists(frames_file):
                    os.makedirs(frames_file)
                if  video_file_path.endswith(".mp4") or  video_file_path.endswith(".mkv"):
                    ffmpeg_path = os.path.join("C:\\", "ffmpeg", "bin", "ffmpeg.exe")
                    subprocess.run([ffmpeg_path,"-i",  video_file_path, "-c:v", "mjpeg", "-q:v", "0", "-pix_fmt", "yuvj420p", ff_path])  
                else:
                    print("El archivo seleccionado no es un video")
                return frames_file
            
            def select_random_images(folder_path):
                images = [img for img in os.listdir(folder_path) if img.endswith(".jpg")]
                return random.sample(images, 4)
            def move_images(images, frames_file, frames_slect):
                for img in images:
                    src_path = os.path.join(frames_file, img)
                    dst_path = os.path.join(frames_slect, img)
                    shutil.copy2(src_path, dst_path)
            def preguntar_texto():
                print("Se ha seleccionado de forma aleatoria 4 imagenes en la ruta ", frames_slect )
                print("Indique la escala para procesar esas 4 imagenes, asi ustede elija el mejor tratamiendo de rudio")
                opcion = input("Elige una relación de escala (2/3/4): ")
                while opcion not in ["2", "3", "4"]:
                    print("Entrada no válida. Por favor, elige una relación de escala válida entre 2,3,4")
                    opcion = input("Elige una relación de escala (2/3/4): ")
                return opcion
            def folder_scale(opcion):
                if opcion == "2":
                    a = 5
                    k_vector = [-1, 0, 1, 2, 3]
                elif opcion == "3" or opcion == "4" :
                    a = 3
                    k_vector = [-1, 0, 3]
                else:
                    print("Opcion no valida.")
                frames_slect_re = []
                for i in range(a):
                    frames_slect_re.append(os.path.join(frames_slect, f'Opcion_{i}'))
                    if os.path.exists(frames_slect_re[i]):
                        shutil.rmtree(frames_slect_re[i])
                    os.makedirs(frames_slect_re[i])
                return a, frames_slect_re, k_vector
            def real_cugan_ncnn_image():
                real_cugan_exe = os.path.join("C:\\", "realcugan-ncnn-vulkan", "realcugan-ncnn-vulkan.exe")
                for i in range(a):
                    c = str(k_vector[i])
                    frames_prueba_fianl= frames_slect_re[i]
                    subprocess.run([real_cugan_exe, "-i", frames_slect, "-o",frames_prueba_fianl, "-n", str(c), "-s", opcion, "-f", "jpg","-c", "3", "-g","0","-j","1:2:2", "-v"])
            def preguntar_texto_2():
                print("En la ruta {frames_slect} existen carpetas enumeradas, el orden de las mismas es el tratamiento de ruido de acuerdo a los parametros disponibles")
                valid_options = ["-1","0","1","2","3"] if opcion == "2" else ["-1", "0", "3"]
                opcion2 = input(f"Elige tratameinto del nivel de ruido {valid_options}: ")
                while opcion2 not in valid_options:
                    print(f"Entrada no válida. Por favor, elige un tratamiento de nivel de ruido válido entre {valid_options}")
                    opcion2 = input("Elige tratamiento del nivel de ruido: ")
                return opcion2
            def real_cugan_ncnn_video():
                image_path  = frames_file
                scaled_path = os.path.join(video_frames_folder, 'frames_finales')
                if not os.path.exists(scaled_path):
                    os.makedirs(scaled_path)
                real_cugan_exe = os.path.join("C:\\", "realcugan-ncnn-vulkan", "realcugan-ncnn-vulkan.exe")
                subprocess.run([real_cugan_exe, "-i", image_path, "-o",  scaled_path , "-n", opcion2, "-s", opcion, "-f", "jpg", "-c", "3", "-g","0","-j","1:2:2", "-v"])
                return scaled_path
            def use_ffmpeg():
                ffprobe_path = os.path.join("C:\\", "ffmpeg", "bin", "ffprobe.exe")
                command = f"{ffprobe_path} -v 0 -of csv=p=0 -select_streams v:0 -show_entries stream=r_frame_rate {video_file_path}"
                result = subprocess.run(command.split(), capture_output=True, text=True)
                framerate = result.stdout.strip()
                command = f"{ffprobe_path} -v 0 -of csv=p=0 -select_streams a -show_entries stream=codec_type {video_file_path}"
                result = subprocess.run(command.split(), capture_output=True, text=True)
                audio_streams = result.stdout.strip().split("\n")
                audio_count = len(audio_streams)
                print("El framerate del video es: ", framerate)
                ffmpeg_path = os.path.join("C:\\", "ffmpeg", "bin", "ffmpeg.exe")
                input_path = os.path.join(scaled_path, "%09d.jpg")
                output_path = os.path.join(video_frames_folder, os.path.splitext(video_file_path)[0]+"4K-RC.mkv")
                if not audio_count  == 0 :
                    subprocess.run([ffmpeg_path, "-i", video_file_path, "-framerate", framerate,"-i", input_path, "-map", "1:v", "-map", "0:a?","-map", "0:s?","-c:v", "libx264", "-preset", "ultrafast", "-tune", "animation", "-profile:v", "high10", "-framerate", framerate, "-c:a", "copy", "-c:s", "copy", output_path])               
                else:
                    subprocess.run([ffmpeg_path, "-r", framerate,"-i", input_path, "-c:v", "libx264", "-preset", "ultrafast", "-tune", "animation", "-profile:v", "high10",  "-r", framerate, output_path])
                    
            def conversion():
                inicio = input("Desea convertir a los frames a video (y/n) ")
                if inicio == "y":
                    use_ffmpeg()
                elif inicio == "n":
                    print("Eso seria todo entonces")
                else:
                    print("Opcion no valida.")
            
            video_file_path = select_video_file()
            video_frames_folder = select_video_folder()
            frames_slect = select_video_frames()
            frames_file= extract_video_frames(video_file_path)
            random_images = select_random_images(frames_file)
            move_images(random_images,frames_file,frames_slect)
            opcion = preguntar_texto()
            a,frames_slect_re, k_vector= folder_scale(opcion)
            real_cugan_ncnn_image()
            opcion2 = preguntar_texto_2()
            scaled_path = real_cugan_ncnn_video()
            conversion()
            
            while True:
                choice_video = input("¿Desea seleccionar otro video? (y/N) ")
                if choice_video == "y" or choice_video == "Y":
                    print("Ok")
                    main_video()
                elif choice_video == "n" or choice_video == "N":
                    break
        

        choice_global = input("¿Desea reescalar una imagen o un video? (I/V) ")
        if choice_global == "I" or choice_global == "i":
            main_image()
        elif choice_global == "v" or choice_global == "V":
            main_video()
main_global()        
while True:
    choice_end = input("¿Desea ejecutar el script de nuevo? (y/N) ")
    if choice_end == "y" or choice_end == "Y":
        print("Ok")
        main_global()
    elif choice_end == "n" or choice_end == "N":
        break
print("Script terminado.")
