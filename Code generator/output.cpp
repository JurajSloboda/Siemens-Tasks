#include "modules/TestDevice.hpp"
#include "iolink/iolink.hpp"

#define True true
#define False false

DeviceAB::DeviceAB(uint8_t slot):
    Module(slot, "IODevice")
{

    initItems();
    initCollections();

}

DeviceAB::~DeviceAB()
{

}

void DeviceAB::initItems()
{
    initDataItem("ProductNumber", 14, "string", 90); 
    initDataItem("SerialNumber", 18, "int", 8); 
    initDataItem("DeviceType", 4275, "bool", 1); 
    initDataItem("test", 10, "bool", 500); 

    // generated code here

}

void DeviceAB::initCollections()
{

    std::shared_ptr<Iolink> Colection = Iolink::getInstance();
    Colection.interface->push("ProductNumber");
    Colection.interface->push("SerialNumber");
    Colection.data->push("DeviceType");
    Colection.tesst->push("test");

    // generated code here

}