extends Button

func _on_toggled(toggled_on: bool) -> void:
	GlobConf.mode = toggled_on
	if toggled_on:
		print("is true")
		print(GlobConf.mode)
	else:
		print("is false")
		print(GlobConf.mode)
