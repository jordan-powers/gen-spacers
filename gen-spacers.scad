TYPE = "hex";
ID = 0.5;
OD = 0.75;
LENGTH = 0.377;
SUBSYSTEM = "IT";
LABEL = "A";

TOLERANCE = 0.005;

text_border = 0.4;

text_depth = LENGTH * 25.4 > 1 ? 0.6 : 0.8 * LENGTH * 25.4;

function text_size(text) = let(
    metrics = textmetrics(text, 1, "Arial Black"),
    k = metrics.size.x * 0.5 / metrics.size.y,
    r2 = (ID + TOLERANCE) * 25.4/2 + text_border,
    r1 = OD * 25.4/2 - text_border
)
((-2 * r2) + 2 * sqrt((r2 * r2) - (((k * k) + 1) * ((r2 * r2) - (r1 * r1))))) / (2 * ((k * k) + 1)) / metrics.size.y;

echo(text_size(SUBSYSTEM), text_size(LABEL));

difference() {
    cylinder(LENGTH * 25.4, d=OD * 25.4, $fn=1024);
    if(TYPE == "hex") {
        #cylinder(LENGTH * 25.4, d=((ID / cos(30)) + TOLERANCE) * 25.4, $fn=6);
    } else if(TYPE == "round") {
        #cylinder(LENGTH * 25.4, d=(ID + TOLERANCE) * 25.4, $fn=1024);
    }
    translate([0, (ID + TOLERANCE) * 25.4 * 0.5 + text_border, LENGTH * 25.4 - text_depth]) {
        #linear_extrude(text_depth) {
                text(SUBSYSTEM, size=text_size(SUBSYSTEM), font="Arial Black", halign="center", valign="bottom");
        }
    }
    translate([0, -(ID + TOLERANCE) * 25.4 * 0.5 - text_border, LENGTH * 25.4 - text_depth]) {
        #linear_extrude(text_depth) {
            text(LABEL, size=text_size(LABEL), font="Arial Black", halign="center", valign="top");
        }
    }
}