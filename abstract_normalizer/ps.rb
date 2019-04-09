require 'pragmatic_segmenter'

fileLocation = ARGV[0]
content = ""
f = File.open("../pragmatic/cache/"+fileLocation, "r")
f.each_line do |line|
	if content == ""
		content += line
	else
		content += line
	end
end
f.close

ps = PragmaticSegmenter::Segmenter.new(text: content)

segments = ps.segment

stringFinal = ""
segments.each do |seg|
	stringFinal += seg + "\n"
end


f = File.open("../pragmatic/"+fileLocation, "w+")
f.write(stringFinal)
f.close