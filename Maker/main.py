from UnityUIfont import UnityUIfont;
from StringHelper import StringHelper;
from PIL import Image, ImageDraw;
import StreamHelper;
import os, csv;

def save_to_csv():
	f = open("OriginalFile/unnamed asset-resources.assets-3177.dat", "rb");
	
	gameobject_pptr = f.read(12);
	enabled = StreamHelper.read_uint32(f);
	momoscript_pptr = f.read(12);
	name = StreamHelper.read_aligned_string(f);
	
	id = StreamHelper.read_aligned_string(f);
	
	txtids_count_en = StreamHelper.read_int32(f);
	txtids_arry_en = [];
	for i in range(txtids_count_en):
		txtids_arry_en.append(StreamHelper.read_aligned_string(f));
	
	txt_count_en = StreamHelper.read_int32(f);
	txt_arry_en = [];
	for i in range(txt_count_en):
		txt_arry_en.append(StreamHelper.read_aligned_string(f));
	
	f.close();

	f = open("OriginalFile/unnamed asset-resources.assets-3187.dat", "rb");
	
	gameobject_pptr = f.read(12);
	enabled = StreamHelper.read_uint32(f);
	momoscript_pptr = f.read(12);
	name = StreamHelper.read_aligned_string(f);
	
	id = StreamHelper.read_aligned_string(f);
	
	txtids_count = StreamHelper.read_int32(f);
	txtids_arry = [];
	for i in range(txtids_count):
		txtids_arry.append(StreamHelper.read_aligned_string(f));
	
	txt_count = StreamHelper.read_int32(f);
	txt_arry = [];
	for i in range(txt_count):
		txt_arry.append(StreamHelper.read_aligned_string(f));
	
	f.close();
	
	f = open("localization.csv", "wb");
	csv_writer = csv.writer(f);
	
	for i in range(txtids_count):
		csv_writer.writerow([txt_arry_en[i], "", txt_arry[i], txtids_arry[i]]);

	f.close();

def csv_to_raw():
	########
	f = open("OriginalFile/unnamed asset-resources.assets-3187.dat", "rb");
	
	gameobject_pptr = f.read(12);
	enabled = StreamHelper.read_uint32(f);
	momoscript_pptr = f.read(12);
	name = StreamHelper.read_aligned_string(f);
	
	id = StreamHelper.read_aligned_string(f);
	
	txtids_count = StreamHelper.read_int32(f);
	txtids_arry = [];
	for i in range(txtids_count):
		txtids_arry.append(StreamHelper.read_aligned_string(f));
	
	txt_count = StreamHelper.read_int32(f);
	txt_arry = [];
	for i in range(txt_count):
		txt_arry.append(StreamHelper.read_aligned_string(f));
	
	others = f.read(StreamHelper.get_unread_data_size(f));
	
	f.close();
	
	########
	f = open("localization.new.csv", "rb");
	csv_reader = csv.reader(f);
	
	txt_arry = [];
	for row in csv_reader:
		txt_arry.append(row[1]);
	f.close();

	########
	f = open("PunchClub/unnamed asset-resources.assets-3187.dat", "wb");
	
	f.write(gameobject_pptr);
	StreamHelper.write_uint32(f, enabled);
	f.write(momoscript_pptr);
	StreamHelper.write_aligned_string(f, name);
	StreamHelper.write_aligned_string(f, id);
	
	StreamHelper.write_int32(f, txtids_count);
	for i in range(txtids_count):
		StreamHelper.write_aligned_string(f, txtids_arry[i]);

	StreamHelper.write_int32(f, txt_count);
	for i in range(txt_count):
		StreamHelper.write_aligned_string(f, txt_arry[i]);
	
	f.write(others);
	
	f.close();

def modify_ui_atlas_pos():
	########
	f = open("OriginalFile/unnamed asset-resources.assets-3376.dat", "rb");
	
	gameobject_pptr = f.read(12);
	enabled = StreamHelper.read_uint32(f);
	momoscript_pptr = f.read(12);
	name = StreamHelper.read_aligned_string(f);
	
	material_pptr = f.read(12);

	uisprite_data_count = StreamHelper.read_int32(f);
	uisprite_data_1_name = StreamHelper.read_aligned_string(f);
	uisprite_data_1_x = StreamHelper.read_int32(f);
	uisprite_data_1_y = StreamHelper.read_int32(f);
	uisprite_data_1_width = StreamHelper.read_int32(f);
	uisprite_data_1_height = StreamHelper.read_int32(f);
	uisprite_data_1_border_left = StreamHelper.read_int32(f);
	uisprite_data_1_border_right = StreamHelper.read_int32(f);
	uisprite_data_1_border_top = StreamHelper.read_int32(f);
	uisprite_data_1_border_bottom = StreamHelper.read_int32(f);
	uisprite_data_1_padding_left = StreamHelper.read_int32(f);
	uisprite_data_1_padding_right = StreamHelper.read_int32(f);
	uisprite_data_1_padding_top = StreamHelper.read_int32(f);
	uisprite_data_1_padding_bottom = StreamHelper.read_int32(f);
	
	others = f.read(StreamHelper.get_unread_data_size(f));
	
	f.close();
	
	f = open("PunchClub/unnamed asset-resources.assets-3376.dat", "wb");
	
	f.write(gameobject_pptr);
	StreamHelper.write_uint32(f, enabled);
	f.write(momoscript_pptr);
	StreamHelper.write_aligned_string(f, name);
	
	f.write(material_pptr);
	
	StreamHelper.write_int32(f, uisprite_data_count);
	StreamHelper.write_aligned_string(f, uisprite_data_1_name);
	StreamHelper.write_int32(f, 0);
	StreamHelper.write_int32(f, 0);
	StreamHelper.write_int32(f, 1024);
	StreamHelper.write_int32(f, 512);
	StreamHelper.write_int32(f, 0);
	StreamHelper.write_int32(f, 0);
	StreamHelper.write_int32(f, 0);
	StreamHelper.write_int32(f, 0);
	StreamHelper.write_int32(f, 0);
	StreamHelper.write_int32(f, 0);
	StreamHelper.write_int32(f, 0);
	StreamHelper.write_int32(f, 0);
	
	f.write(others);
	
	f.close();
	
def gen_font_image():
	bmfc_filepath = "Font/cn_12.bmfc";
	output_filepath = "Font/cn_12.fnt";

	# min text
	sh = StringHelper();
	sh.add_file_text("localization.new.csv");
	sh.add_western();
	f = open("Font/textmin.txt", "wb");
	f.write(sh.get_chars().decode("utf-8").encode("utf-8-sig"));
	f.close();

	# Can't add " ", make sure the path have no space.
	bmfont_tool_path = "E:\\BMFont\\bmfont.com";
	text_file_path = "\"Font\\textmin.txt\"";
	bmfc_filepath = "\"" + bmfc_filepath.replace("/", "\\") + "\"";
	output_filepath = "\"" + output_filepath.replace("/", "\\") + "\"";
	commandstr = " ".join((bmfont_tool_path , "-c" ,bmfc_filepath, "-o", output_filepath, "-t" ,text_file_path));
	os.system(commandstr.encode('mbcs'));

def gen_combined_image():
	gen_font_image();
	modify_ui_atlas_pos();
	
	im1 = Image.open("Font/cn_atlas-resources.assets-124.png");
	im2 = Image.open("Font/cn_12_0.png");
	imc = Image.new('RGBA', (1024, 1024), 'red');
	
	imc.paste(im1.convert("RGBA").crop());
	imc.paste(im2.convert("RGBA").crop(), (0, 0, im2.size[0], im2.size[1]));
	
	imc.save("PunchClub/cn_atlas-resources.assets-124.png");
	
def gen_ngui_font():
	gen_combined_image();

	uifont = UnityUIfont("OriginalFile/unnamed asset-resources.assets-3394.dat", version = 17);
	uifont.read_from_bmfont("Font/cn_12.fnt", fullsize = [1024, 1024], xadvance_increasment = 1);

	# related to NGUItext.
	uifont.bmfont_spritename = "cn_12_0";
	uifont.bmfont_size = 16;

	for i in range(len(uifont.bmfont_saved_arry)):
		uifont.bmfont_saved_arry[i]["offsetY"] += 3;
	
	uifont.symbols_arry.append("(_icon_stm)");
	uifont.symbols_arry.append("font_stm");
	uifont.symbols_arry.append("(_icon_agl)");
	uifont.symbols_arry.append("font_agl");
	uifont.symbols_arry.append("(_icon_str)");
	uifont.symbols_arry.append("font_str");
	uifont.symbols_count += 3;
	
	uifont.save_to_raw("PunchClub/unnamed asset-resources.assets-3394.dat");
	
csv_to_raw();
gen_ngui_font();