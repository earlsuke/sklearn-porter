# -*- coding: utf-8 -*-

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.utils import shuffle
from sklearn_porter import Porter


iris_data = load_iris()
X, y = iris_data.data, iris_data.target

X = shuffle(X, random_state=0)
y = shuffle(y, random_state=0)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=5)

clf = MLPClassifier(
    activation='tanh', hidden_layer_sizes=50, max_iter=500, alpha=1e-4,
    solver='sgd', tol=1e-4, random_state=1, learning_rate_init=.1)

clf.fit(X_train, y_train)

output = Porter(clf).export()
# output = Porter(clf, language='java').export()
print(output)

"""
class Brain {

    // Type: tanh
    public static double[] compAct(double[] v) {
        for (int i = 0, l = v.length; i < l; i++) {
            v[i] = Math.tanh(v[i]);
        }
        return v;
    }

    // Type: softmax
    public static double[] compOut(double[] v) {
        double max = Double.NEGATIVE_INFINITY;
        for (double x : v) {
            if (x > max) {
                max = x;
            }
        }
        for (int i = 0, l = v.length; i < l; i++) {
            v[i] = Math.exp(v[i] - max);
        }
        double sum = 0.0;
        for (double x : v) {
            sum += x;
        }
        for (int i = 0, l = v.length; i < l; i++) {
            v[i] /= sum;
        }
        return v;
    }

    public static int predict(double[] atts) {
        if (atts.length != 4) { return -1; }
    
        double[][] activations = {atts, new double[50], new double[3]};
        double[][][] coefficients = {{{-0.16871183680139706, 0.17222254135180864, -0.3913644197291774, -0.2096851298032836, -0.21196657452183515, -0.21691233507903898, -0.21159659266837222, -0.18418924586861396, 0.3514706440528485, -0.14917414881541816, 0.011252952050632165, 0.13082185689846668, -0.31548139474569775, 0.23632851727123275, -0.31325477263892443, 0.12273968950399096, -0.3401067290755887, 0.18127383600019864, -0.34192591519440535, -0.24712952612794986, 0.31807517718147965, 0.20680543277142543, -0.074640609143509312, 0.049727650329561605, 0.10344749532476341, 0.17106393973130932, -0.16344484601935935, -0.41178123787878007, -0.024666408074548257, 0.14339362493611479, -0.22105446023125436, 0.26113593136708452, 0.29933866674525861, -0.32288074642242726, -0.070041513702141484, -0.14382058169927411, 0.38421514879586588, 0.25141403516319449, -0.32504253860458276, 0.232996113197597, 0.3913673360885625, 0.11001510315621411, -0.014112583174551909, 0.25058157657251662, -0.058017193185767049, -0.088590506518301096, 0.34816565204943511, 0.10500104411331394, -0.10325765108171235, -0.046588138805641284}, {-0.42903758481544602, 0.15602074262118362, -0.21052541680287079, -0.21242562380213614, -0.03469706864093268, -0.27586007398844448, 0.047976615193086797, -0.39836435408927418, 0.36973084133771039, 0.034013761269885402, -0.22770589546653744, -0.14668228250422555, -0.051564172235077435, -0.054770277672274589, -0.29883701095054721, -0.0059821841596954493, 0.10015603409770681, 0.11047344171210383, 0.13990896174940476, 0.020333973758368876, 0.45852686963961431, -0.39685750800520114, -0.20419596976571502, 0.27033819750943511, -0.15021268027844809, -0.25752294993507863, 0.43038721796740331, -0.12648850347153748, 0.47027930698187814, 0.1302078788004698, 0.28001572294190863, 0.34625896597354328, 0.16455046017059347, -0.34169364399831731, -0.37366236751311327, 0.20951556867352397, 0.11134281572360728, 0.31219849671340766, 0.10029662047847557, 0.12293093024913464, -0.16721653441189679, 0.43736224294079856, 0.062759417493591749, 0.012174893116597269, 0.10067370116467467, -0.24986501287850466, 0.30198366908924873, 0.39485976020405816, -0.30938329459277103, 0.22949109239262905}, {-0.082935927208133392, -0.013912087037484474, 0.16590330746521598, -0.10599000700591754, 0.45672500347277828, 0.12703108060585491, -0.32366437045770363, 0.50618500817542322, 0.17818067444118807, 0.24796046431977467, -0.18887068811981039, 0.10322054706554352, 0.47500321382646188, 0.10222640686886239, -0.28878547648351022, 0.20710364869608977, -0.28132950444496363, 0.31101455425343766, 0.31595099647902058, -0.25157155243382523, -0.75874430190638853, -0.074269617830893669, -0.30640398620965886, -0.45719618582145083, 0.16813896526547678, -0.028184179330902, -0.19073012886154656, 0.10743133783906518, -0.5450807379576188, -0.38900089770527735, 0.073500045383612905, 0.31636646007599423, 0.036643949304858925, -0.403234598170917, 0.45136782652649599, -0.16849714200811255, 0.27534599475271382, -0.034445854680072212, 0.35926134669818255, 0.18796665063101714, -0.03953037403959192, -0.64285038056445565, -0.26560271775552946, -0.027814962652193027, -0.28556986458593009, -0.20497864276007149, -0.15183376543158847, -0.29258274366815101, 0.018849205056939673, -0.29142882412957755}, {-0.26493490324972768, 0.29718317490209845, -0.00065342573046086694, -0.19543317245653741, -0.056503001745312732, 0.17543460771659275, -0.20316119876188893, 0.1593843689209386, 0.29958270646368879, 0.21093378165713272, -0.16656159530197107, 0.19559014772153413, 0.1734162371778934, 0.209380963088311, -0.22870860684358729, -0.32485719851617439, -0.44560175557449833, -0.0080258303619293158, 0.15942574652920516, 0.048401060835388345, -0.40172681365669094, 0.47131945757836874, 0.053065476076209352, -0.19878006252754937, 0.01797383788242669, 0.16080150922931782, -0.036567211222579742, -0.19541651920828679, -0.42516525051576781, -0.21938304175479964, 0.084579946520297558, -0.20679898693130316, 0.16734941258228139, -0.2987331146300673, 0.010840585350357007, 0.1783145378660857, -0.20879033714721673, 0.10593840194296868, 0.11219807812634679, 0.28757819652222699, -0.19419033130594454, -0.45652102247079013, 0.160178148667842, 0.28542389516836847, 0.26696636644712218, 0.31149363198878144, -0.33179549050999507, -0.42222387973839215, 0.050136882850502336, 0.30228679151009408}}, {{-0.33847551673844545, 0.25987859298049676, -0.019823379849720664}, {0.31545714654646706, 0.12345932401305892, 0.17165459014952208}, {-0.060227174816852164, 0.050563567527544116, 0.0018334977997186627}, {0.060849228883097642, 0.1091392456031311, 0.29780473349835068}, {-0.10342520292172498, 0.19258830723211154, 0.46102912990391093}, {-0.18678726912371432, 0.065875908820848816, 0.083459129126681228}, {-0.056069980692588416, -0.14573677750139571, -0.0038418976769160965}, {-0.71698880694168499, 0.16696741906189322, 0.4622393440016232}, {0.22657239402117063, 0.20566201733509379, -0.19659602925527547}, {-0.080753372347669633, -0.038760801393972213, 0.16506148468839446}, {0.24656373768630477, 0.21792348019691152, 0.17247214483285744}, {0.058722200942261694, -0.066853624759574154, -0.074319530038484766}, {-0.42142312281426592, 0.17286818117531702, 0.51931396304364863}, {0.098275699989940304, 0.094989671033000905, 0.15869749606099959}, {-0.0053142776962164691, -0.077475207994424172, 0.00019309428176925852}, {-0.31240502711955137, -0.069034180840924109, -0.27414681261388169}, {0.29990881982972373, -0.14479437330080788, 0.16538980562721636}, {0.20000618466572159, 0.21524977529862113, 0.010614569385245867}, {-0.31232286662189085, -0.13767514234518688, 0.095384895546369086}, {-0.19121154707546811, -0.0070970732827304803, -0.050791851529645576}, {0.92883383199675118, 0.079119183756214725, -0.61560059871487471}, {-0.28562041034089225, -0.1905750027140774, 0.0074649243163665419}, {0.1172045789040783, -0.25243551203469983, -0.076864311958216691}, {0.61043626182394017, -0.055103916955106046, -0.29679260317445155}, {-0.22138980514925644, -0.19794764308604637, -0.017057737279932431}, {-0.096771605690832568, -0.15060362595107074, 0.080234552423727748}, {0.19950652839323818, -0.054034882135648568, -0.25132669685966202}, {0.098326236791060881, -0.20115732144575302, 0.098072718903017789}, {0.59052161903734024, -0.35620097413721447, -0.48196272941472335}, {0.39975722014353315, 0.23336910069420624, -0.12434982735035546}, {0.29141463403976636, 0.20768741824674966, 0.26992543653635392}, {0.089865805770482393, -0.12669660929133264, 0.10692430789156829}, {0.18282528259678424, 0.12733792472322952, 0.10258790363951739}, {-0.28165125735865804, 0.096051317072508163, 0.21018747136445312}, {-0.45116542288485978, -0.0075014093277201502, 0.22251963318629933}, {0.24204189792790318, -0.080524179826459763, -0.10227895885618479}, {0.084521023632667558, 0.4030069131617442, -0.10162871274208846}, {-0.18837077602406957, 0.31300418786390133, -0.066847304298536081}, {0.14223851679532229, 0.18159494413212685, 0.4199168125035978}, {0.048998030739356706, 0.082330776881080869, -0.32787221036306846}, {-0.17206091791187569, -0.22025382659497916, -0.25212818063425424}, {0.74189978797089706, -0.44012762834777636, -0.5422873034964355}, {0.29992503254675335, 0.080602797083445255, 0.12144782016989639}, {-0.085036935402644662, -0.081596329385539734, -0.027088013056969645}, {0.32572947041627781, -0.22858010658959951, -0.13658865385164726}, {-0.13728490341556687, 0.10263728555594757, 0.014002981598803199}, {-0.13996628373298384, 0.030391475335891753, -0.37667338053924937}, {0.25108030005413706, -0.096396909342872997, -0.40800981885862858}, {-0.0097383259124461385, 0.19539305370456861, 0.028528364676480178}, {0.26209147851495135, -0.028952002272874044, -0.029950155605217195}}};
        double[][] intercepts = {{0.27329993209430209, 0.045310867633656354, 0.27288324760831439, 0.077849850445091434, -0.08678817617553182, -5.4942767215827209e-05, 0.069049906095333638, -0.001351882234418093, 0.37269129695600306, 0.24642350794307871, -0.057710905515910849, 0.27602091532766571, -0.25701844183485578, -0.25086548614215542, -0.24291339229998862, 0.0058787688780131157, -0.35095977227260644, 0.32759995581220519, 0.1820224617249597, -0.33311222928102641, -0.14338741581704045, -0.15890098532849142, -0.23565265831762289, 0.21039815571773038, -0.13135057234436923, 0.27459945142322323, 0.10236286853974209, 0.23734657497494971, 0.29179121899019184, 0.27022356890602728, -0.016817592366898296, 0.097021609456156704, 0.19801869110809275, -0.21204201739373746, -0.074780231104254274, 0.066208351573373847, -0.2692023201710636, 0.066055748646204768, -0.061275656952743306, 0.21793674702065699, -0.10428472854774561, 0.2793289505623322, 0.078508256139697211, -0.21688633895597972, 0.23537233053629866, 0.059800248313777858, -0.28090048094084513, 0.038273387641640809, 0.13206836674617714, 0.31958941316477846}, {0.36240186249890116, 0.25839314565174937, -0.42179831644378363}};
    
        for (int i = 0; i < activations.length - 1; i++) {
            for (int j = 0; j < activations[i + 1].length; j++) {
                for (int l = 0; l < activations[i].length; l++) {
                    activations[i + 1][j] += activations[i][l] * coefficients[i][l][j];
                }
                activations[i + 1][j] += intercepts[i][j];
            }
            if ((i + 1) < (activations.length - 1)) {
                activations[i + 1] = Brain.compAct(activations[i + 1]);
            }
        }
        activations[activations.length - 1] = Brain.compOut(activations[activations.length - 1]);
    
        int class_idx = -1;
        double class_val = Double.NEGATIVE_INFINITY;
        for (int i = 0, l = activations[activations.length - 1].length; i < l; i++) {
            if (activations[activations.length - 1][i] > class_val) {
                class_val = activations[activations.length - 1][i];
                class_idx = i;
            }
        }
        return class_idx;
    }

    public static void main(String[] args) {
        if (args.length == 4) {
            double[] atts = new double[args.length];
            for (int i = 0, l = args.length; i < l; i++) {
                atts[i] = Double.parseDouble(args[i]);
            }
            System.out.println(Brain.predict(atts));
        }
    }
}
"""
