echo [replace nlog.xml]
.\dgregister.exe replace_placeholder --config .\sample\Config.json --file .\sample\Base\nlog.xml --output .\done\nlog.xml

echo [replace appsettings-shared.json]
.\dgregister.exe replace_placeholder --config .\sample\Config.json --file .\sample\Base\appsettings-shared.json --output .\done\appsettings-shared.json

echo [replace devp-2-1.json]
.\dgregister.exe replace_placeholder --config .\sample\Config.json --file .\sample\DevP\devp-2-1.json --output .\done\devp-2-1.json

echo [replace appsettings.json]
.\dgregister.exe replace_placeholder --config .\sample\Config.json --file .\sample\DevP\appsettings.json --output .\done\appsettings.json

echo [replace smes-7-0-development.json]
.\dgregister.exe replace_placeholder --config .\sample\Config.json --file .\sample\sMES\smes-7-0-development.json --output .\done\smes-7-0-development.json

echo [replace smes-7-0-production.json]
.\dgregister.exe replace_placeholder --config .\sample\Config.json --file .\sample\sMES\smes-7-0-production.json --output .\done\smes-7-0-production.json

pause