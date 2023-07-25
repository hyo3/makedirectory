import os
import shutil

before_word = "演習14.1"

def rename_files(before_word, after_word, path):

    files_list = []
    dirs_list = []
    
    for curdir, dirs, files in os.walk(path):
        for file_name in files:
            
            before_file_name = os.path.join(curdir,file_name)
            after_file_name = os.path.join(curdir, file_name.replace(before_word, after_word))
            files_list.append([before_file_name, after_file_name])
                        
        for dir_name in dirs:
            
            before_dir_name = os.path.join(curdir, dir_name)
            after_dir_name = os.path.join(curdir, dir_name.replace(before_word, after_word))
            dirs_list.insert(0, [before_dir_name, after_dir_name])
            
    for before_file_name, after_file_name in files_list:
        os.rename(before_file_name, after_file_name)
        
    for before_file_name, after_file_name in dirs_list:
        os.rename(before_file_name, after_file_name)

        
def replace_word_in_file(file_path, before_word, after_word):
        
    with open(file_path, encoding="utf-8") as f:
        data_lines = f.read()

    # 文字列置換
    data_lines = data_lines.replace(before_word, after_word)

    # 同じファイル名で保存
    with open(file_path, mode="w", encoding="utf-8") as f:
        f.write(data_lines)

lesson_count = input("授業回数：")
practice_num = input("演習の個数：")
assignment_num = input("課題の個数：")


if practice_num != 0:
    
    for num in range(int(practice_num)):
        num += 1
    
        #ファイル名に含まれる変更したい単語と変更後の単語
        
        after_word  = "演習" + lesson_count + "." + str(num)
        
        source_dir_path      = "C:\\Users\\hyo\\source\\repos\\" + before_word
        destination_dir_path = "C:\\Users\\hyo\\source\\repos\\" + after_word
        
        if os.path.exists(destination_dir_path) != True:
            
            shutil.copytree(source_dir_path, destination_dir_path) 
            shutil.rmtree(destination_dir_path + "/.vs")
            rename_files(before_word, after_word, destination_dir_path)
            print("{}を作成しました。".format(after_word))
            
            files_name = [destination_dir_path + "/" + after_word + ".sln",
                          destination_dir_path + ("/" + after_word) * 2 + ".vcxproj"]

            for file in files_name:
                
                replace_word_in_file(file, before_word, after_word)
                replace_word_in_file(file, before_word.replace(".", ""), after_word.replace(".", ""))
                
if assignment_num != 0:
    
    for num in range(int(assignment_num)):
        num += 1
        
    #ファイル名に含まれる変更したい単語と変更後の単語

        after_word = "課題" + lesson_count + "." + str(num)
    
        source_dir_path      = "C:\\Users\\hyo\\source\\repos\\" + before_word
        destination_dir_path = "C:\\Users\\hyo\\source\\repos\\" + after_word
        
        if os.path.exists(destination_dir_path) != True:
        
            shutil.copytree(source_dir_path, destination_dir_path)
            shutil.rmtree(destination_dir_path + "/.vs")
            rename_files(before_word, after_word, destination_dir_path)
            print("{}を作成しました。".format(after_word))
            
            files_name = [destination_dir_path + "/" + after_word + ".sln",
                          destination_dir_path + ("/" + after_word) * 2  + ".vcxproj"]

            for file in files_name:
                
                replace_word_in_file(file, before_word, after_word)
                replace_word_in_file(file, before_word.replace(".", ""), after_word.replace(".", ""))