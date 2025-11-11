from huggingface_hub import snapshot_download
if __name__ == "__main__":
	snapshot_download(
		repo_id="Qwen/Qwen3-VL-2B-Instruct", 
		local_dir="/home/chwenjun225_laptop/projects/Scientific_Image_Forgery_Detection/models/Qwen3-VL-2B-Instruct", 
		revision="main"
	)