import json
import argparse
import os
def get_transcript(json_filename):
    with open(json_filename,"r") as file:
        jsonData = json.load(file)

    # Final transcript string
    final_transcript = ""

    for result in jsonData["results"]:
        for alternative in result["alternatives"]:
            if "transcript" in alternative:
                final_transcript += alternative["transcript"] + " "
    return final_transcript

if __name__=="__main__":
    parser = argparse.ArgumentParser("transcript configuration")
    parser.add_argument("-ifp","--input-file-path",help="Path to input json folder")
    parser.add_argument("-ofp","--output-file-path", default="z_transcripts",help="Path to output txt folder")
    args = parser.parse_args()
    input_folder = args.input_file_path
    output_folder= args.output_file_path
    for folder_name in os.listdir(input_folder):
        folder_path = os.path.join(input_folder, folder_name)
        for filename in os.listdir(folder_path):
            if filename.split(".")[-1] != "json":
                continue
            input_path = os.path.join(folder_path, filename)
            transcript = get_transcript(input_path)
            output_filename = "transcript_"+filename.replace("json","txt")
            output_path = os.path.join(output_folder, output_filename)
            with open(output_path, "w") as fw:
                fw.write(transcript)
