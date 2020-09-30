# frozen_string_literal: true
#
# A Ruby script to create BagIT for embargoed items from fedora commons
#

bag_export_path = '/data0/hydra/shared/tmp/bags/etd/'

export_work_list = ARGV[0]
year = ARGV[1]
workids_file = File.join(File.dirname(__FILE__), export_work_list)
work_to_export = []
File.readlines(workids_file).each do |line|
  work_to_export.push(line.chomp.strip)
end
work_to_export.sort!
puts "A total of #{work_to_export.length} Fedora works to export."

bag_export_path += year
puts "Bag export path #{bag_export_path}"

work_to_export.each do |work_id|
  puts "#{work_id}"
  bag_dir_path = File.join(bag_export_path, work_id)
  Dir.mkdir(bag_dir_path) unless Dir.exist?(bag_dir_path)
  fedora_dir = work_id[0,2] + '/' + work_id[2,2] + '/' + work_id[4,2] + '/' + work_id[6,2] + '/' + work_id
  command = "java -jar fcrepo-import-export-0.1.0.jar --mode export --resource " + "http://localhost:8080/fcrepo/rest/prod/" + fedora_dir + " --dir " + bag_dir_path + " --binaries --predicate http://pcdm.org/models#hasMember,http://www.w3.org/ns/ldp#contains --bag-profile default --bag-config metadata.yml"
  puts "#{command}"
  system(command)
end
puts "DONE"
