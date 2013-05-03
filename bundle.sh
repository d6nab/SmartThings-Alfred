rm SmartThings.alfredworkflow
rm .DS_Store

cd alfredworkflow
rm .DS_Store
rm alfred/.DS_Store

zip -r SmartThings ../LICENSE ./* 
mv SmartThings.zip ../SmartThings.alfredworkflow

cd ../
